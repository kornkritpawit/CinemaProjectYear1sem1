from lastproject.shape import *
from lastproject.cinemaclass import *
def login():
    file = open('admin.txt').read()
    welcome()
    to()
    Yim()
    world()
    print('|')
    print('Y')
    print('Y')
    while True:
        admin = input('Enter your position (C)ustomer or (A)dmin: ').upper()
        if admin == 'A':
            count = 0
            while True:

                pas = input('Enter password to confirm yourself: ')
                if pas != file:
                    count += 1
                    print(f'attempt left({5-count})')
                    if count == 5:
                        exit('You are trying to hack!!!!\nYou are fired!!!!!!')
                else:
                    loading()
                    print('   ||')
                    print('   ||')
                    print('   \/')
                    return 'Admin'

        elif admin == 'C':
            loading()

            return 'Customer'

def menu1(a,cin):
    if a=='Admin':
        new=[x.get_book() for x in cin if len(x.get_book())>0]
        if len(new)>0:
            print('(m)ovies\n(r)eports\n(l)ogout\n(e)xit')
            return 1
        else:
            print('(m)ovies\n(l)ogout\n(e)xit')
            return 0
    elif a=='Customer':
        if len(cin)>0:
            print('(m)ovies\n(b)ooking\n(l)ogout\n(e)xit')
            return 1
        else:
            print('(m)ovies\n(l)ogout\n(e)xit')
            return 0

def menu2(a):
    def newmov():
        name = input('Movie name: ')
        while True:
            try:
                seat = int(input('Seat capacity: '))
                break
            except (TypeError, ValueError):
                print('input number!!!!')

        mov = movie(name, seat)
        a.append(mov)
        print()
        moviesss(a)

        # menu1(a)
    while True:
        if len(a)==0:
            print('(n)ew movie')
            print('(m)ain menu')
            chose = input('Choose a menu: ').lower()
            if chose == 'n':
                newmov()
            elif chose=='m':
                break
            else:
                print('type m or n')
        elif len(a)>0:
            print('(n)ew movie\n(d)elete movie\n(m)ain menu')
            chose = input('Choose a menu: ').lower()
            if chose=='n':
                newmov()

            elif chose=='d':
                while True:
                    try:
                        while True:
                            num = int(input('Movie number: '))
                            if 0<num<=len(a):
                                break
                            print('input in movie number!!!!')


                        break
                    except (TypeError, ValueError):
                        print('input number!!!!')
                del a[num-1]
                moviesss(a)
            if chose=='m':
                break


def book_sum(a):
    print("Bookings Summary")
    for i in range(len(a)):
        print(f'{i+1}. {a[i].showremain()}')



def moviesss(a):
    if len(a)==0:
        print('No movies')
    elif len(a)>0:
        print('Movie Summary')
        for i in range(len(a)):
            print(f'{i+1}. {a[i]}')
        print()

def show_reserve(a):
    if len(a)==0:
        print('No Booking')
    elif len(a)>0:
        for i in range(len(a)):
            print(f'{i+1}. {a[i]}')
def delete_item(mov,a):
    while True:
        if len(a)<=0:
            'No Booking'
            break
        choose = input('delete item number or (b)ack: ').lower()

        if choose.isnumeric():

            if 0 < int(choose) <= len(a):
                mov.unreserve(int(choose)-1)
                # del a[int(choose)-1]
                print()
                print(mov.showremain())

                show_reserve(a)
                print(f'Total {mov.show_book()} seats')

        elif choose == 'b':
            break

def report(a):
        book_sum(a)
        print()
        while True:
            choose=input('Enter a movie number or (m)ain menu: ').lower()
            if choose.isnumeric():

                if 0<int(choose)<=len(a):
                    print()
                    print(a[int(choose)-1].showremain())
                    show_reserve(a[int(choose)-1].get_book())
                    print(f'Total {a[int(choose)-1].show_book()} seats')
                    delete_item(a[int(choose)-1],a[int(choose)-1].get_book())



            elif choose=='m':
                break







