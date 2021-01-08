def print_triangle_withdeco(num, char='%'):
    if 0 < num <10:
        for i in range(0, num):
            for j in range(0, num-i+1):
                print(end=' ')
            for k in range(0, i+1):
                print(char, end='')
            print()
    else:
        return 0
print_triangle_withdeco(2)
print_triangle_withdeco(5, '*')