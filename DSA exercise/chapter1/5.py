def max(arr,num):
    if num==1:
        return arr[0]
    mx=max(arr,num-1)
    if mx>arr[num-1]:
        return mx
    else :return arr[num-1]
arr=[1,45,5,2,3,2,4,2]
print(max(arr,8))