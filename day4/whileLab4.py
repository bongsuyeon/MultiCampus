while True:
    month = int(input("월을 입력하시오"))
    if month == 12 or month == 1 or month == 2:
        print(month,"월은 겨울")
    elif month == 3 or month == 4 or month == 5:
        print(month,"월은 봄")
    elif month == 6 or month == 7 or month == 8:
        print(month,"월은 여름")
    elif month == 9 or month == 10 or month == 11:
        print(month,"월은 가을")
    else:
        print("1~12 사이의 값을 입력하세요!")
        break