from datetime import datetime
from plyer import notification
import threading
import pygame
import time
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

#音声を流す関数
pygame.mixer.init()
def play_sound(file):
  try:
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    print(f"{file}を再生中…")
    #音が再生中なら待機(1秒ごとに確認)
    while pygame.mixer.music.get_busy():
      time.sleep(0.1)
    print("再生完了！")
  except Exception as e:
    print(f"再生エラー: {e}")


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
          sound_file = os.path.join(base_dir, "yasumi.wav")
        elif "時出勤" in event:
          sound_file = os.path.join(base_dir, "osoban.wav")
        elif "" in event:
          sound_file = os.path.join(base_dir, "oshigoto.wav")
        break
except FileNotFoundError:
  message = "予定ファイルが見つからなかったよ！"

#音声を別スレッドで再生
threading.Thread(target=play_sound, args=(sound_file,),daemon=True).start()

#通知を表示
notification.notify(
  title = "｛ぽにゃまるん❣️)",
  message=message,
  timeout=180
)

# 音声をスレッドで再生
if sound_file:
  threading.Thread(target=play_sound, args=(sound_file,), daemon=True).start()
