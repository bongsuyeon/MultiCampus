class Member:
    count = 0  # 클래스 변수 초기화
    def __init__(self):
        self.name = None
        self.account = None
        self.passwd = None
        self.brithyear =None
    # 클래스 변수에 값 설정
        Member.count += 1
        print("회원 {} :".format(Member.count),end=' ')

obj1 = Member()
obj1.name = "kim"
obj1.account = "KIMS"
obj1.passwd = "kims1234"
obj1.brithyear = 1999
print(obj1.name, "(", obj1.account, obj1.passwd, obj1.brithyear,")")

obj2 = Member()
obj2.name = "lee"
obj2.account = "LEES"
obj2.passwd = "lees1234"
obj2.brithyear = 1994
print(obj2.name, "(",obj2.account, obj2.passwd, obj2.brithyear,")")

obj3 = Member()
obj3.name = "park"
obj3.account = "PARKS"
obj3.passwd = "parks1234"
obj3.brithyear = 1990
print(obj3.name,"(", obj3.account, obj3.passwd, obj3.brithyear,")")
