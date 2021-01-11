a = [['B', 'C', 'A', 'A'],
    ['C', 'C', 'B', 'B'],
    ['D', 'A', 'A', 'D']]

b = [['A',0],
     ['B',0],
     ['C',0],
     ['D',0]]

for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        if a[i][j] == 'A':
            b[0][1] += 1
        elif a[i][j] == 'B':
            b[1][1] += 1
        elif a[i][j] == 'C':
            b[2][1] += 1
        elif a[i][j] == 'D':
            b[3][1] += 1

for i in range(0, len(b)):
    print(b[i][0], "는", b[i][1], "개 입니다.")
