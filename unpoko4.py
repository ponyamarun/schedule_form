import time
import os
import random
import keyboard #キーボード入力をキャッチするやつ

def clear():
    os.system ('cls' if os.name=='nt' else'clear')

count=0

print("うんぽこ増殖スタート❣️")
print("「へそまる」を呼びたくなったら、キーボードの【H】を押して止めてね！")
time.sleep(2)

while True:
    clear()
    print("うんぽこ増殖中……💩💩💩\n")
    for _ in range(count):
        spaces=""*random.randint(0,50)
        count+=1
        time.sleep(0.3)

        if msvcrt.kbhit():
            key=msvcrt.getch()
            if key.lower()==b'h':
                clear()
                print("✨へそまる登場～！うんぽこ止めたよ！✨")
                break