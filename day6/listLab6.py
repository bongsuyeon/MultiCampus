a = [[10, 12, 14, 16], [18, 20, 22, 24], [26, 28, 30, 32], [34, 36, 38, 40]]

#1행 1열의 데이터 : 10
print(a[0][0])

# 3행 4열의 데이터 : 32
print(a[2][3])

#행의 갯수 : 4
print(len(a))

#열의 갯수 : 4
print(len(a[0]))

#3행의 데이터들 : 26 28 30 32
print(a[2])

#2열의 데이터들 : 12 20 28 36
for i in range(0, len(a)-1):
        print(a[i][1],end=', ')
print(a[len(a)-1][1])

#왼쪽 대각선 데이터들 : 10 20 30 40
for i in range(len(a)-1):
    print(a[i][i], end=', ')
print(a[len(a)-1][len(a)-1])

#오른쪽 대각선 데이터들 : 16 22 28 34
for i in range(len(a)):
    print(a[i][len(a)-1-i], end=', ')





