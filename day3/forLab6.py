result = 0
for i in range (1, 51):
    if(i % 5 == 0):
        continue
    elif(i % 3 == 0):
        result += i
print("결과 = ", result)