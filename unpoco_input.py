import streamlit as st
from datetime import date
import os

st.markdown("# うんぽこスケジューラー \n## シフト入力フォーム💩")

#日付を選ぶ
selected_date = st.date_input("日付を選んでね❣️",value=date.today())

#出勤パターンを選ぶ
shift_type = st.radio("シフトを選んでね❣️",("通常出勤","休み","遅番"))

event = "" #デフォルト(通常出勤は空白)

#遅番の時だけ時間を指定
if shift_type == "遅番":
  hour = st.selectbox("何時に出勤？",list(range(17,20))) #17～20時
  event = f"{hour}時出勤"
elif shift_type == "休み":
  event = "休み"

#ファイルパスを明示＆登録ボタン
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir,"schedule.txt")
if st.button("この内容で登録✨💩✨"):
  try:
    file_path = "schedule.txt"
    with open(file_path,"a",encoding="utf-8") as f:
      f.write(f"{selected_date},{event}\n")
    st.success("登録できたよ❣️")
  except Exception as e:
    st.error(f"エラーが発生しちゃったよ…: {e}")