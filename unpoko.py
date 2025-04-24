#うんぽこが一匹ずつ増えていく
import time
import os

#うんぽこカウント
count=0

#ぽこぽこ出すループ
while True:
    count+=1
    print("💩"*count)
    time.sleep(0.1) #n秒ごとに増える(n秒待機)
    if count >=30:
        break