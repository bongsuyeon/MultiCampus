while True:
    word = input("문자열을 입력하시오 :")
    wordlength = len(word)
    if wordlength == 0:
        break
    elif wordlength >= 5 and wordlength < 9:
        continue
    elif wordlength < 5:
        print("유효한 입력 결과:", "*", word, "*")
    elif wordlength > 8:
        print("유효한 입력 결과:", "$", word, "$")
