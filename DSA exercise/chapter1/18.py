def duplicate(str,start,end):
    if end-start==1:
        if str[start]==str[end]:
            return True
    
    mid=(end+start)//2
    for i in range(start,mid):
        if str[mid+i]!=str[i]:
            return False
    
    return duplicate(str,start+1,mid-1)
    
print(duplicate('allall',0,6))    
