def average(arr,n):
    if n==1:
        return arr[0]
    result= ( average(arr,n-1)* (n-1)+ arr[n-1] )/n
    return result
