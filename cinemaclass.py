class movie:
    def __init__(self,movie,seat,cost):
        self.__initseat=seat
        self.__movie=movie
        self.__seat=seat
        self.__totalreserve=0
        self.__book=[]
        self.__cost=cost
        self.__receive=0

    def movie(self):
        return f'{self.__movie:<15} {str(self.__seat):3} seats'
    def movie_summary(self):
        return f'{self.__movie:<15} {str(self.__seat):3} seats / Remaining  {self.__total_seat:3} seats'
    def get_moviename(self):
        return self.__movie
    def get_cost(self):
        return self.__cost
    def get_book(self):
        return self.__book
    def get_seat(self):
        return self.__seat
    def get_receive(self):
        return self.__receive
    def show_book(self):
        return self.__totalreserve
    def reserve(self,bok):
        self.__book.append(bok)
        self.__seat-=bok.get_reserve()
        self.__totalreserve+=bok.get_reserve()
        self.__receive+=(self.__cost*bok.get_reserve())


    def unreserve(self,num):
        self.__seat+=self.__book[num].get_reserve()
        self.__totalreserve-=self.__book[num].get_reserve()
        self.__receive-=self.__cost*self.__book[num].get_reserve()
        del self.__book[num]
    def __str__(self):
        return f'{self.__movie:<15} {self.__initseat} seats'
    def showremain(self):
        return f'{self.__movie:<15} {self.__initseat} seats / Remaining {self.__seat} seats'

class booking:
    def __init__(self,name,seat):
        self.__name=name
        self.__movie= movie
        self.__reserve=seat
    def __str__(self):
        return f'{self.__name:<6}{self.__reserve:<2} seats'
    def get_reserve(self):
        return self.__reserve
    def get_index(self):
        return self.__movie

class customer:
    def __init__(self,name):
        self.__person=name
        self.__money=0
    def get_money(self):
        return self.__money
    def add_money(self,money):
        self.__money+=money
    def pay(self,cost):
        self.__money-=cost
