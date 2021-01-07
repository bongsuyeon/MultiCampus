import random

def differtwovalue(n,m):
    if n > m:
        return n-m
    else:
        return m-n

i = 0
while i < 5:
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    print(num1, "와", num2, "의 차는", differtwovalue(num1, num2), "입니다")
    i += 1
