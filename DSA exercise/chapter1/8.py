def table(arr,n):
    if n==0:
        print(*arr)
        return 
    arr.append(0)
    table(arr,n-1)
    arr.pop()
    arr.append(1)
    table(arr,n-1)
    arr.pop()
table([],3)
