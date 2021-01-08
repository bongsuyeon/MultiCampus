def sumAll(*p):
    CheckNotInt = True
    for check in p:
        if str(type(check)) == "<class 'int'>":
            CheckNotInt = False
    if p == () or CheckNotInt == True:
        return None
    sum = 0
    for data in p:
        if str(type(data)) != "<class 'int'>":
            continue
        sum += data
    return sum


print(sumAll())
print(sumAll(1, 2, 3, 4, 5, 6, 7))
print(sumAll(2, 4, 'b', 'A', 0))
print(sumAll('09876543', 'D'))
