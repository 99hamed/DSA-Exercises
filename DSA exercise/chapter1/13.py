def hanoi(n,S,A,D):
    if n==1:
         print(f'{S}---->{D}')
    else:
        hanoi(n-1,S,D,A)
        print(f'{S}---->{D}')
        hanoi(n-1,A,S,D)
    
hanoi(3,'S','A','D')    