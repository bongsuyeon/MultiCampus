def print_gugudan(n):
    if str(type(n)) != "<class 'int'>":
        print(type(n), "ss")
        return 0
    elif n <= 0 or n > 10:
        return 0
    else:
        for i in range(1, 10):
            print(i, "*", n, "=", i*n)

num = int(input("입력 :"))
print_gugudan(num)