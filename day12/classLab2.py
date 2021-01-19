class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def getBookInfo(self):
        b = "책이름: "+self.title +"\n저자: "+ self.author+"\n가격: "+ str(self.price)
        return b

obj1 = Book("파이썬정복","김상형", 19800)
print(obj1.getBookInfo()+"\n-----------------")
obj2 = Book("달러구트 꿈 백화점","이미예", 12420)
print(obj2.getBookInfo()+"\n-----------------")
obj3 = Book("2030 축의 전환","미우로 기옌", 16200)
print(obj3.getBookInfo()+"\n-----------------")
obj4 = Book("공정하다는 착각","마이클샌덴", 16200)
print(obj4.getBookInfo()+"\n-----------------")
obj5 = Book("시선으로부터","정세랑", 12600)
print(obj5.getBookInfo())



