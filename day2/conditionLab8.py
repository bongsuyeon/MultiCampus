import random

def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a , b):
    return a*b
def div(a, b):
    return a/b
def re(a, b):
    return a%b

oper_num = random.randint(1,10)
print(oper_num)
if oper_num % 5 == 1:
    anw = add(300, 50)
elif oper_num % 5 == 2:
    anw = sub(300, 50)
elif oper_num % 5 == 3:
    anw = mul(300, 50)
elif oper_num % 5 == 4:
    anw = div(300, 50)
elif oper_num % 5 == 0:
    anw = re(300, 50)

print("결과값 :", anw)