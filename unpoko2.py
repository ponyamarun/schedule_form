#うんぽこ増殖中
import time
import os

count=0
while True:
    count+=1
    os.system('cls' if os.name=='nt' else'clear')#画面クリア
    print("うんぽこ増殖中…")
    print("💩"*count)
    time.sleep(0.5)
    if count >=30:
        break