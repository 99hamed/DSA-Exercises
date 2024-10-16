def hanoi(n,S,A,D):
    if n==1:
         print(f'{S}---->{A}')
         print(f'{A}---->{D}')
    else:
        hanoi(n-1,S,A,D)
        print(f'{S}---->{A}')
        print(f'{A}---->{D}')
        hanoi(n-1,S,A,D)
        hanoi(n-1,A,S,D)
hanoi(2,'S','A','D')    