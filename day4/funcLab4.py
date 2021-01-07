def print_triangle(n):
    if n <= 0 or n > 10:
        return 0
    else:
        for i in range(0, n):
            for j in range(0, i+1):
                print("*", end='')
            print("")


num = int(input("1-10 사이 숫자 입력:"))
print_triangle(num)
