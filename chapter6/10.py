def sort_k(arr,k): # with selection sort
    n = len(arr)
    for i in range(k):
        min= i
        
        for j in range(i,n):
            if arr[j] <arr[min]:
               min= j
        print(arr[min])
        arr[i], arr[min] = arr[min], arr[i]
        
    return
sort_k([4,2,3,9,11,6,8,12],4)