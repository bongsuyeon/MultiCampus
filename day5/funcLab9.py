def sumEven1(*p):
    if p == ():
        return -1
    sum = 0
    for data in p:
        if data % 2 == 0:
            sum += data
    return sum


print(sumEven1())
print(sumEven1(1, 2, 3, 4, 5, 6, 7))
print(sumEven1(1, 3, 5, 7, 9))
print(sumEven1(2, 4, 6, 8, 0))
