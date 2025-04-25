from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import re
from datetime import datetime


app = Flask(__name__)

# ここにぽにゃまるんのチャネルシークレットとアクセストークンを入れてね！
LINE_CHANNEL_ACCESS_TOKEN = 'JUQmHy8xRA0+/mSy7pSHpBQdplHDnn8Cm6hlCFdSGRyzM82GmTAFd0Ih0VaDwrZYHA4VzrFfc4E1w8SVlfbcpuYWIi6x/stn9HrQLGe8dBmaEdsYSqtEU4/fB8kOQnjlrWoayNduoPVamiooMrxFugdB04t89/1O/w1cDnyilFU='
LINE_CHANNEL_SECRET = '91bdd2dcce2572a95abb8c659c1bb252'

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

def parse_schedule_message(text):
    #日付部分のパターン(4/27や5月1日など)
    date_pattern = r'(\d{1,2}[\/月]\d{1,2}[日]?)'
    match = re.search(date_pattern,text)

    if not match:
        return None #日付がないと判断
    
    date_str = match.group(1)
    try:
        #色々な日付形式に対応
        if '月' in date_str:
            date_obj = datetime.strptime(date_str.replace('日',''), '%m月%d')
        else:
            date_obj = datetime.strptime(date_str, '%m/%d')
    except ValueError:
        return None
    
    #今年の年を補完(例：2025)
    date_obj = date_obj.replace(year=datetime.now().year)
    date_formated = date_obj.strftime('%Y-%m-%d')

    #残りのテキストを予定とみなす
    task = text.replace(date_str, '').strip()
    return date_formated, task

#schedule.txtファイルに追記
def write_schedule(date , task):
    #taskが辞書やリストでなく、文字列だけになるように明示
    task_str = str(task).strip()
    if task_str.startswith("{"):
        task_str = task_str.strip("{}[]'\"")
    date_str = str(date).strip()
    if date_str.startswith("{"):
        date_str = task_str.strip("{}[]'\"")
    with open("schedule.txt", "a", encoding="utf-8") as f:
        f.write(f"{date_str},{task_str}\n")

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    received_text = event.message.text
    #handle_messageの中で呼び出す準備
    parsed = parse_schedule_message(event.message.text)

    if parsed:
        date, task = parsed
        write_schedule(date,task)
        reply = f"ぽにゃまるん、予定を記録したよ～❣️\n『{date} : {task}』っと…メモメモ📝"
    else:
        reply = f"ぽにゃまるん、'{received_text}を受け取ったよ❣️"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply)
    )

if __name__ == "__main__":
    app.run()
