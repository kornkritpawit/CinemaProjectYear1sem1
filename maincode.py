from lastproject.customerfunction import *

cin=[]
customname=[]
customclass=[]
while True:
    status,index=login(customname,customclass)
    print(f'As a {status}')
    if status=='Admin':
        while True:
            a=menu1(status,cin,customclass,index)
            choose=input('Choose a menu: ').lower()
            if a==4:
                if choose=='m':
                    clear()
                    moviesss(cin)
                    menu2(cin)

                elif choose=='l':
                    clear()
                    logout()
                    break
                elif choose=='e':
                    exit('BYE-BYE Yeahขอบคุณที่ทำให้รู้ว่ารักเราคืออะไร\niักกันขนาดนี้ไปลงนรกด้วยกันเลยไป')

            elif a==1:
                if choose=='m':
                    clear()
                    moviesss(cin)
                    menu2(cin)

                elif choose=='l':
                    clear()
                    logout()
                    break
                elif choose=='e':
                    exit('BYE-BYE Yeahขอบคุณที่ทำให้รู้ว่ารักเราคืออะไร\niักกันขนาดนี้ไปลงนรกด้วยกันเลยไป')
                elif choose=='r':
                    report(cin)
                elif choose=='c':
                    showcustomer(customname)
                    deletecustomer(customname,customclass)
            elif a==2:
                if choose=='m':
                    clear()
                    moviesss(cin)
                    menu2(cin)

                elif choose=='l':
                    clear()
                    logout()
                    break
                elif choose=='e':
                    exit('BYE-BYE Yeahขอบคุณที่ทำให้รู้ว่ารักเราคืออะไร\niักกันขนาดนี้ไปลงนรกด้วยกันเลยไป')
                elif choose=='r':
                    report(cin)
                elif choose=='c':
                    showcustomer(customname)
                    deletecustomer(customname,customclass)
            elif a==3:
                if choose=='m':
                    clear()
                    moviesss(cin)
                    menu2(cin)

                elif choose=='l':
                    clear()
                    logout()
                    break
                elif choose=='e':
                    exit('BYE-BYE Yeahขอบคุณที่ทำให้รู้ว่ารักเราคืออะไร\niักกันขนาดนี้ไปลงนรกด้วยกันเลยไป')
                elif choose=='c':
                    showcustomer(customname)
                    deletecustomer(customname,customclass)



    elif status=='Customer':
        while True:

            a=menu1(status,cin,customclass,customclass[index])
            choose=input('Choose a menu: ').lower()
            if a==5:
                if choose=='a':
                    insertmoney(customclass[index])
                elif choose=='b':
                    clear()
                    book(cin,customclass[index])
                elif choose=='m':
                    clear()
                    moviesss(cin)
                elif choose=='l':
                    clear()
                    logout()
                    break
                elif choose=='e':
                    exit('BYE-BYE Yeahขอบคุณที่ทำให้รู้ว่ารักเราคืออะไร\niักกันขนาดนี้ไปลงนรกด้วยกันเลยไป')
                else:
                    print('choose (b) or (m) or (l) or (e)')
            elif a==6:
                if choose=='a':
                    insertmoney(customclass[index])
                elif choose=='m':
                    clear()
                    moviesss(cin)
                elif choose == 'l':
                    clear()
                    logout()
                    break
                elif choose=='e':
                    exit('BYE-BYE Yeahขอบคุณที่ทำให้รู้ว่ารักเราคืออะไร\niักกันขนาดนี้ไปลงนรกด้วยกันเลยไป')
                else:
                    print('choose (m) or (l) or (e)')















