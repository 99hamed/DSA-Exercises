def find(a,b):
    if b>a:
        a,b=b,a
    if(a%b==0): return b
    return find(b,a%b)
print(find(20,12))        
        