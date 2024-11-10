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
                elif a[i] <= b[i]:
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
    def multiply(self,other):
        
        a = list(reversed(self.value))
        b = list(reversed(other.value))
        result_sign = self.sign * other.sign
        result = [0] * (len(a) + len(b))

        for i in range(len(a)):
            for j in range(len(b)):
                result[i + j] += a[i] * b[j] #normal multiply
                result[i + j + 1] += result[i + j] // 10 # add dahgan to next number
                result[i + j] %= 10 # add yekan to curr number

        result.reverse()
        while len(result) > 1 and result[0] == 0:
            result.pop(0)

        result_obj = BigNumber("0")
        result_obj.value = result
        result_obj.sign = result_sign
        
        return result_obj
    def karatsuba(self, x, y):
        # return base condition multiply
        if len(x) == 1 or len(y) == 1:
            return str(int(x) * int(y))

        n = max(len(x), len(y))
        half = n // 2
       
        # filling string untill max lentgh
        x+='0'*(n-len(x))
        y+='0'*(n-len(y))

       # divide string 
        x1=x[:-half]
        x0=x[-half:]
        y1=y[:-half]
        y0= y[-half:]

        
        z2 = self.karatsuba(x1, y1)
        z0 = self.karatsuba(x0, y0)
        z1 = self.karatsuba(str(int(x1) + int(x0)), str(int(y1) + int(y0)))
        z1 = str(int(z1) - int(z2) - int(z0))

          
        result = int(z2) * 10**(2 * half) + int(z1) * 10**half + int(z0)
        return str(result)

    def karatsuba_multiply(self, other):
        result_sign = self.sign * other.sign
        x_str = ''.join(map(str, self.value))
        y_str = ''.join(map(str, other.value))
        
        result_value = self.karatsuba(x_str, y_str)
        
        result = BigNumber(result_value)
        result.sign = result_sign
        
        return result

     
    def divide(self, other):
        if other.value == [0]:
            raise ValueError("Division by zero is not allowed.")
        
      
        result_sign = self.sign * other.sign

        
        dividend = BigNumber(''.join(map(str, self.value))) # maqsoom
        divisor = BigNumber(''.join(map(str, other.value))) # maqsoom alahi
        dividend.sign = divisor.sign = 1

        
        if  self.compare(dividend.value,divisor.value)==False:
            return BigNumber("0")

        quotient = []
        remainder = BigNumber("0")

        for digit in dividend.value:
            remainder = BigNumber(str(remainder) + str(digit))

            
            count = 0
            while self.compare(remainder.value,divisor.value) :
                remainder = remainder.sub(divisor)
                count += 1

            quotient.append(count)
        
        while len(quotient) > 1 and quotient[0] == 0:
            quotient.pop(0)
    
        result = BigNumber(''.join(map(str, quotient)))
        result.sign = result_sign
        
        return result

    def factorial(self,other):
      
        if other.sign < 0:
            raise Exception("Factorial is not defined for negative numbers.")
    
        result = BigNumber('1')
        current = BigNumber('1')
    
        while current.compare(current.value,other.value) ==False:
            result = result.multiply(current)
            current = current.add(BigNumber('1'))
    
        return result

    
    
    def power(self, exponent):
        result = BigNumber("1")
        base = BigNumber(str(self))

        while exponent > 0:
            if exponent % 2 == 1:
                result = result.multiply(base)
            base = base.multiply(base)
            exponent //= 2

        return result


num1 = BigNumber(input('Enter first number: '))
num2 = BigNumber(input('Enter your second number: '))


res1=num1.sub(num2)
res2=num1.add(num2)
res3=num1.multiply(num2)
print("Subtract:", res1)
print("Sum:", res2)
print('multiply:',res3)
print('katsuba multiply:',num1.karatsuba_multiply(num2))
print('power:',num1.power(int(input('input your exponent of power:',))))
num3 = BigNumber(input('Enter your factorial number: '))
print('fact:',num1.factorial(num3))
print('divide:',num1.divide(num2))
num1.shiftL(5)
num2.shiftR(5)
print("shiftL:", num1)
print("ShiftR:", num2)
