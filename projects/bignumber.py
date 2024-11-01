class BigNumber():
    # for initielize value with array type
    def __init__(self,num):
        self.value=[int(i) for i in num]
    # change array type to string
    def __str__(self):
        return ''.join(map(str,self.value))
    
    def add(self,other):
        result=[]
        carry=0
        # because add end till first
        a=list(reversed(self.value))
        b=list(reversed(other.value))

        maxlen=max(len(a),len(b))
        a += [0] * (maxlen- len(a))
        b += [0] * (maxlen - len(b))
        
        for i in range(maxlen):
            temp=a[i]+b[i]+carry 
            carry=temp/10
            result.append(temp%10)
        if carry>0:
            result.append(carry)
        # for deleting 0 before number
        while(len(result)>1 and result[-1]==0):
            result.pop()
        result.reverse()
       
        return BigNumber(result)
    
    def subtract(self,other):
        
        result=[]
        carry=0
        
        a=list(reversed(self.value))
        b=list(reversed(other.value))

        maxl=max(len(a),len(b))
        a += [0] * (maxl- len(a))
        b += [0] * (maxl - len(b))
            
        for i in range(maxl):
            temp=a[i]-b[i]-carry 
            if temp<0:
                temp+=10
                carry=1
            else:
                carry=0
            result.append(temp)
        
        while len(result) > 1 and result[-1] == 0:
            result.pop()    
        
        
        result.reverse()
        return BigNumber(result)
    
    def shiftR(self, shift_count):
        if shift_count >= len(self.value):
            self.value = [0]
        else:
            self.value = self.value[:len(self.value)-shift_count]
        
    def shiftL(self, shift_count):
        
        if self.value != [0]:  
            self.value += [0] * shift_count

    




num1 = BigNumber("47545455353")
num2 = BigNumber("95452524254")


res1=num1.subtract(num2)
res2=num1.add(num2)
print("Subtract:", res1)
print("Sum:", res2)
num1.shiftL(5)
num2.shiftR(4)
print("shiftL:", num1)
print("ShiftR:", num2)
