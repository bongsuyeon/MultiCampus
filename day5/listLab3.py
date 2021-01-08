listnum = [10, 5, 7, 21, 4, 8, 18]

minNum = listnum[0]

for i in range(0, len(listnum)):
    if minNum > listnum[i]:
        minNum = listnum[i]

print("최솟값 :", minNum)