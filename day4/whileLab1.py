import random

num = 1
endNum = random.randint(5, 10)

while num < endNum:
    print(num,'->',num*num)
    num += 1
