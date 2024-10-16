def divide(a,b,counter=0):
    if b==0:
      raise Exception('division zero')  
    elif a==0:
       return counter
    counter+=1
    return divide(a-b,b,counter)
    
print(divide(15,5))

