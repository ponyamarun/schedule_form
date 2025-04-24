from datetime import datetime
from plyer import notification
import threading
import pygame

#音声を流す関数
pygame.mixer.init()
def play_sound(file):
  pygame.mixer.music.load(file)
  pygame.mixer.music.play()


#ファイル名とデフォルトメッセージ
filename = "schedule.txt"
default_message  = "今日は16時出勤だよ❣️"
sound_file=""
message = default_message

#今日の日付を取得(YYYY-MM-DD形式)
today = datetime.now().strftime("%Y-%m-%d")

#ファイルから予定を読み込む
try:
  with open(filename, "r", encoding="utf-8") as file:
    for line in file:
      date,event = line.strip().split(",")
      if date == today:
        #eventが空だったらデフォメを使う
        if event.strip() == "":
          message = default_message
        else:
          message = f"今日は{event}だよ❣️"

        #音声ファイルを切り替える
        if "休み" in event:
          play_sound("yasumi.wav")
        elif "時出勤" in event:
          play_sound("osoban.wav")
        elif "" in event:
          play_sound("oshigoto.wav")
        break
except FileNotFoundError:
  message = "予定ファイルが見つからなかったよ！"

#通知を表示
notification.notify(
  title = "💩｛ぽにゃまるん❣️)",
  message=message,
  timeout=180
)

# 音声をスレッドで再生
if sound_file:
  threading.Thread(target=play_sound, args=(sound_file,), daemon=True).start()
