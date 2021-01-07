def expr(num1, num2, char):
    if char == '+':
        return num1 + num2
    elif char == '-':
        return num1 - num2
    elif char == '/':
        return num1 / num2
    elif char == '*':
        return num1 * num2
    else:
        return "None"

n = int(input("숫자1 입력:"))
m = int(input("숫자2 입력:"))
c = input("연산자 입력:")

result = expr(n, m, c)

if result == 'None':
    print("수행불가")
else:
    print("연살결과 :", result)
