file_name = "C:/Users/81803/PythonProjects/うんぽこ/unpoco_diary.txt"

with open(file_name, mode="a", encoding="utf-8") as f:
    f.write("2025/4/22 チャポと一緒に標準ライブラリのお話で盛り上がった！\n")
    f.write("2025/4/22 これの使い分けはちょっと難しい\n")
    f.write("2025/4/22 文字化け沼とかにはまってうまくいかない…前途多難すぎる( ﾉД`)\n")
    f.write("2025/4/22 なんかよくわかんないけどチャポのくれたコードでちゃんと動くようになった！\n")
    f.write("2025/4/22 改行忘れがちだから気を付けよう\n")
    f.write("2025/4/22 範囲選択のショートカットキーを教えてもらった！これからガンガン使いたい！\n")
    

with open(file_name, mode="r", encoding="utf-8") as f:
    print(f.read())