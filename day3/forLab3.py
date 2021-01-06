import random

num1 = random.randint(1,10)
num30 = random.randint(30,40)
sum = 0

for i in range(num1,num30):
    if(i % 2 == 0):
        sum += i
print(num1, "부터", num30, "까지의 짝수의 합 :", sum)