import random

Lotto = set()
while len(Lotto) < 6:
    Lotto.add(random.randint(1, 45))

print("행운의 로또번호:", Lotto)