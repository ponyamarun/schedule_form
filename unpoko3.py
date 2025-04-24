import time
import os
import random

def clear():
    os.system('cls' if os.name=='nt' else'clear')

width=60 #横幅の目安
height=10 #行数の目安
poop_count=0
max_poop=50

poop_positions=[]

while poop_count < max_poop:
    clear()
    poop_positions.append((random.randint(0,height-1),random.randint(0,width-1)))

    for y in range(height):
        line=""
        for x in range(width):
            if(y,x)in poop_positions:
                line+="💩"
            else:
                line+=""
        print(line)

    poop_count+=1
    time.sleep(0.2)
       
