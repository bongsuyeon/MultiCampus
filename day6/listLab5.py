import random

Lotto = []

while len(Lotto) < 6:
    Lotto.append(random.randint(1, 45))
    my_set = set(Lotto)  # 집합set으로 변환
    Lotto = list(my_set)  # list로 변환

print("행운의 로또번호:", Lotto)
