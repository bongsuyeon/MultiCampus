listnum = [10, 5, 7, 21, 4, 8, 18]

maxNum = listnum[0]

for i in range(0, len(listnum)):
    if maxNum <listnum[i]:
        maxNum = listnum[i]

print("최댓값 :", maxNum)