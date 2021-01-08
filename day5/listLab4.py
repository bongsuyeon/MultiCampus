import random
listnum = []

for i in range(0, 10):
    listnum.append(random.randint(1,50))

print(listnum)

for i in range(0, 10):
    if listnum[i] < 10 :
        listnum[i] = 100
print(listnum)


# 인덱싱 방법으로 listnum의 첫 번째 데이터를 출력한다.
print(listnum[0])

# 인덱싱 방법으로 listnum의 마지막 데이터를 출력한다.
print(listnum[9])

# 슬라이싱 방법으로 listnum의  두 번째 데이터부터 여섯 번째 데이터만 추출하여 출력한다.
print(listnum[1:6])

# 슬라이싱 방법으로 listnum의 데이터를 역순으로 출력한다.
print(listnum[len(listnum):0:-1])

# 슬라이싱 방법으로 listnum의 데이터를 모두 출력한다.
print(listnum[0:len(listnum)])

# 인덱싱 방법으로 5번째 데이터를 삭제한다.
print("delte:", listnum.pop(4))

# 슬라이싱 방법으로 listnum의 데이터를 모두 출력한다.
print(listnum[0:len(listnum)])

# 슬라이싱 방법으로 2~3번째 데이터를 삭제한다.
listnum[1:3] = []

# 슬라이싱 방법으로 listnum의 데이터를 모두 출력한다
print(listnum[0:len(listnum)])




