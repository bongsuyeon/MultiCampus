while True:
    num = int(input("입력 값 : "))
    if num == 0 :
        print("종료")
        break
    elif num < -10 or num > 10:
        continue
    elif num < 0:
        num *= -1
        print("입력 값(부호변경):", num)
    if num > 0 and num <= 10:
        mul = 1
        while num > 1:
            mul *= num
            num -= 1
        print(mul)