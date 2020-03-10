from lastproject.Adminfunction import *

def book(a,customer):
    print(f'Your money is {customer.get_money()}')
    book_sum(a)
    print()
    while True:
        print('(b)ook\n(m)ain menu')
        choose= input('Choose a menu: ')
        if choose=='b':
            name=input('Name: ')
            while True:
                try:
                    while True:
                        num = int(input('Movie: '))
                        if 0 < num <= len(a):
                            break
                        print('input in movie number!!!!')
                    break
                except (TypeError, ValueError):
                    print('input a number!!!!')

            while True:
                try:
                    while True:
                        seat= int(input('Amount: '))
                        if 0<seat<a[num-1].get_seat():
                            break
                        print('Too much seat')
                    break
                except (TypeError,ValueError):
                    print('input number!!!!')
            bok=booking(name,seat)
            a[num-1].reserve(bok)
            total=a[num-1].get_cost()*seat
            print(f"Total cost = {total} baht ")
            customer.pay(total)
            print(f'Your money is {customer.get_money()}')

            print()
            book_sum(a)

            print()
        elif choose=='m':
            print()
            break
        else:
            print('type m or b')

def insertmoney(a):
    while True:
        print()
        print(f'Your money is {a.get_money()}')
        print('insert(1000) banknote or (500) banknote or (100) banknote\n(50) banknote (20) banknote or (b)ack')
        choose=input('insert :').lower()
        if choose=='1000':
            while True:
                n=input('How many notes you want to insert? : ')
                if n.isnumeric():
                    a.add_money(1000*int(n))
                    break
                else:
                    print('input number only!!!')
        elif choose=='500':
            while True:
                n=input('How many notes you want to insert? : ')
                if n.isnumeric():
                    a.add_money(500*int(n))
                    break
                else:
                    print('input number only!!!')
        elif choose=='100':
            while True:
                n=input('How many notes you want to insert? : ')
                if n.isnumeric():
                    a.add_money(100*int(n))
                    break
                else:
                    print('input number only!!!')
        elif choose=='50':
            while True:
                n=input('How many notes you want to insert? : ')
                if n.isnumeric():
                    a.add_money(50*int(n))
                    break
                else:
                    print('input number only!!!')
        elif choose=='20':
            while True:
                n=input('How many notes you want to insert? : ')
                if n.isnumeric():
                    a.add_money(20*int(n))
                    break
                else:
                    print('input number only!!!')

        elif choose=='b':
            print()
            break
        else:
            print('choose again')











