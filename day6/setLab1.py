import random

set_1 = set()
set_2 = set()

while len(set_1) < 10:
    set_1.add(random.randint(1, 20))
while len(set_2) < 10:
    set_2.add(random.randint(1, 20))

print(set_1)
print(set_2)
print(set_1 | set_2)
print(set_1 - set_2)
print(set_2 - set_1)
print((set_1 | set_2) - (set_2 & set_1))