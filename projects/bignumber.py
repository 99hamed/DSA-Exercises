class BigNumber:
    def __init__(self, value):
        if value[0] == '-':
            self.sign = -1
            self.value = [int(digit) for digit in value[1:]]
        else:
            self.sign = 1
            self.value = [int(digit) for digit in value]
    # to show array as a string
    def __str__(self):
        return ('-' if self.sign == -1 else '') + ''.join(map(str, self.value))
    # compare if first is bigger for - and +
    def compare(self, a, b):
        
        if len(a) > len(b):
            return True
        elif len(a) < len(b):
            return False
        else:
            for i in range(len(a)):
                if a[i] > b[i]:
                    return True
                elif a[i] < b[i]:
                    return False
            return True  

    def add_operation(self, a, b):
        result = []
        carry = 0
        # reverse for add members from yekan
        a = list(reversed(a))
        b = list(reversed(b))

        maxlen = max(len(a), len(b))
        a += [0] * (maxlen - len(a))
        b += [0] * (maxlen - len(b))

        for i in range(maxlen):
            temp = a[i] + b[i] + carry
            carry = temp // 10  
            result.append(temp % 10)
        
        if carry > 0:
            result.append(carry)
        # for remove 0 before number
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        result.reverse()
        return result

    def add(self, other):
        # baraye jam adad ham alamat
        if self.sign == other.sign:
            result_value = self.add_operation(self.value, other.value)
            result_sign = self.sign
        else:
            
            if self.compare(self.value, other.value):
                result_value = self.subtract_operation(self.value, other.value)
                result_sign = self.sign
            # agar adad manfi bozorg tar bood sign manfi mishavad
            else:
                result_value = self.subtract_operation(other.value, self.value)
                result_sign = other.sign

        result = BigNumber('0')
        result.value = result_value
        result.sign = result_sign
        return result
   
    def subtract_operation(self, a, b):
        result = []
        carry = 0

        a = list(reversed(a))
        b = list(reversed(b))
        maxl = max(len(a), len(b))
        a += [0] * (maxl - len(a))
        b += [0] * (maxl - len(b))

        for i in range(maxl):
            temp = a[i] - b[i] - carry
            if temp < 0:
                temp += 10
                carry = 1
            else:
                carry = 0
            result.append(temp)

        while len(result) > 1 and result[-1] == 0:
            result.pop()

        result.reverse()
        return result
    
    def sub(self,other):
        if self.sign == other.sign:
           # manfi normal
            if self.compare(self.value,other.value):
                result_value = self.subtract_operation(self.value, other.value)
                result_sign = self.sign
            # adad dovomi bozorg tar bashad alamat gharine mishavad
            else:
                result_value = self.subtract_operation(other.value, self.value)
                result_sign = -self.sign
        else:
            
            result_value = self.add_operation(self.value, other.value)
            result_sign = self.sign

        result = BigNumber("0")
        result.value = result_value
        result.sign = result_sign
        
        return result
    def shiftR(self, n):
        if n >= len(self.value):
            self.value = [0]
        else:
            self.value = self.value[:-n]

    def shiftL(self, n):
        if self.value != [0]:
            self.value+=[0]*n
            

num1 = BigNumber(input('Enter first number: '))
num2 = BigNumber(input('Enter your second number: '))


res1=num1.sub(num2)
res2=num1.add(num2)
print("Subtract:", res1)
print("Sum:", res2)
num1.shiftL(4)
num2.shiftR(4)
print("shiftL:", num1)
print("ShiftR:", num2)
