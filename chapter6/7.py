def find_max2(arr): # with selection sort 
    n = len(arr)
    for i in range(2):
        max = i
        
        for j in range(n-i-1,-1,-1):
            if arr[j] > arr[max]:
               max = j
        
        arr[n-i-1], arr[max] = arr[max], arr[n-i-1]

    return arr[n-2]
print(find_max2([4,2,3,9,11,6,8,12]))