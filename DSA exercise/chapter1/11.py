def money(n,i=0,j=0,k=0):
    money(n,i+1,j,k)

    money(n,i,j,k+1)
    if i*2 + j*10+k*5==n:
                    print(f'{j} *10 + {k}*5 + {i}*2')
    if i<=n :
        return money(n,i,j+1,k)         
    
  
                   
money(20)
