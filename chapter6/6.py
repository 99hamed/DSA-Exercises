def insertion_array(arr,m,n):
    for i in range(m):
        for j in range(1,n):
            k=j-1
            temp=arr[i][j]
            while k>=0 and arr[i][k]>temp:
                arr[i][k+1]=arr[i][k]
                k-=1
            arr[i][k+1]=temp
    return arr
array=[[5,2,78,5],[5,3,4,7],[45,8,3,5]]
m=len(array)
n=len(array[0])

for i in insertion_array(array,m,n):
    print(i)
    

