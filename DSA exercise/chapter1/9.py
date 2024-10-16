def fact(n):
    if n==1:
        return n
    res=fact(n-1)*n
    return res
def sum(n):
    if n==1:
        return fact(1)
    res=fact(n)+sum(n-1)
    return res
print(sum(4))