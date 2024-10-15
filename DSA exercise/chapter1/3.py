def reverse(arr,index):
    if index<=len(arr)//2-1:
        arr[index],arr[len(arr)-index-1]=arr[len(arr)-index-1],arr[index]
        reverse(arr,index+1)
    return arr
print(reverse([1,5,4,5,6,8],0))