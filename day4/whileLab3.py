import random

randomNum = random.randint(0, 30)
Char = "0ABCDEFGHIJKLMNOPQRSYUVWXYZ"
count = 0

while randomNum > 0 and randomNum < 27:
    print("(", Char[randomNum], ")", randomNum)
    count += 1
    randomNum = random.randint(0, 30)

print("수행횟수는", count, "번입니다")