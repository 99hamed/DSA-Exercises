def findbinary(number,result):
    if number==0:
        return  result
    result=str(number%2) + result
    return findbinary(number//2,result)
print(findbinary(3,""))
