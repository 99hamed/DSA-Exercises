import numpy as np
import matplotlib.pyplot as plt

# Stack class for operators
class Stack:
    def __init__(self):
        self.items = [0] * 20
        self.top = -1

    def push(self, item):
        self.top += 1
        self.items[self.top] = item

    def pop(self):
        if not self.is_empty():
            self.top -= 1
            return self.items[self.top + 1]
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[self.top] 
            
        return None

    def is_empty(self):
        return self.top == -1

class infix_convertor:
    # taghadom operator
    def operator_precedence(self,op1, op2):
        if op1==op2:
            return False
        if  op2==None:
            return True
        if op1=='*' or op1=='/' and op2=='+' or op2=='-':
            return True
        if op1=='+' or '-' and op2=='*' or '/':
            return False
        if op1=='/' or op1=='*' or op1=='-' or op1=='+'or op1=='^' and op2=='(':
            return True
        
    
    def infix_to_postfix(self, expression):
        operators = Stack()
        postfix = ''
        i = 0
        while i < len(expression):
            char = expression[i]
            # Check for negative numbers
            if char.isalnum() or (char == '-' and (i == 0 or expression[i - 1] in "(+*/^")):
                if char == '-':
                    operators.push('~')
                    char=''
                      # Replace with ~ for negative numbers
                num = char
                i += 1
                while i < len(expression) and expression[i].isalnum():
                    num += expression[i]
                    i += 1
                postfix += num + ' '
                continue
            elif char == '(':
                operators.push(char)
            elif char == ')':
                while not operators.is_empty() and operators.peek() != '(':
                    postfix += operators.pop() + ' '
                operators.pop()
            else:  # Operator
                while (not operators.is_empty() and operators.peek() != '(' and
                       self.operator_precedence(operators.peek(), char)):
                    postfix += operators.pop() + ' '
                operators.push(char)
            i += 1

        while not operators.is_empty():
            postfix += operators.pop() + ' '

        return postfix.strip()

    def evaluate_postfix(self, postfix):
        stack = Stack()
        tokens = postfix.split()
        for token in tokens:
            if token in 'x,y,z':
                return Exception(ValueError)
            if token.rstrip('~').isdigit(): 
                stack.push(int(token) if token[0] != '~' else -int(token[1:]))
            else:
                if token == '~':  
                    a = stack.pop()
                    stack.push(-a)
                else:
                    b = stack.pop()
                    a = stack.pop()
                    if token == '+':
                        stack.push(a + b)
                    elif token == '-':
                        stack.push(a - b)
                    elif token == '*':
                        stack.push(a * b)
                    elif token == '/':
                        stack.push(a / b)
                    elif token == '^':
                        stack.push(a ** b)
        return stack.pop()



    def infix_to_prefix(self, expression):
        operators = Stack()
        operands = Stack()
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isalnum() or (char == '-' and (i == 0 or expression[i - 1] in "(+*/^")):
                if char == '-':
                    char = '~'  # Replace with ~ for negative numbers
                num = char
                i += 1
                while i < len(expression) and expression[i].isalnum():
                    num += expression[i]
                    i += 1
                operands.push(num)
                continue
            elif char == '(':
                operators.push(char)
            elif char == ')':
                while not operators.is_empty() and operators.peek() != '(':
                    op = operators.pop()
                    right = operands.pop()
                    left = operands.pop()
                    operands.push(op + left + right)
                operators.pop()
            else:
                while (not operators.is_empty() and operators.peek() != '(' and
                       self.operator_precedence(operators.peek(), char)):
                    op = operators.pop()
                    right = operands.pop()
                    left = operands.pop()
                    operands.push(op + left + right)
                operators.push(char)
            i += 1

        while not operators.is_empty():
            op = operators.pop()
            right = operands.pop()
            left = operands.pop()
            operands.push(op + left + right)

        return operands.pop()
def plot(user):
    # Second part: draw function
    x = np.linspace(-50, 50, 500)
    y = np.linspace(-50, 50, 500)
    x, y = np.meshgrid(x, y)
    z = eval(user)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')

    plt.title(f'Plot of f(x) = {user}')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
    plt.axvline(0, color='black', linestyle='--', linewidth=0.8)
    plt.grid()

    plt.show()

new = infix_convertor()
expression = input('Enter your expression in infix: ')
print("Infix: ", expression)

postfix = new.infix_to_postfix(expression)
print("Postfix: ", postfix)

prefix = new.infix_to_prefix(expression)
print("Prefix: ", prefix)

result = new.evaluate_postfix(postfix)
print("Result: ", result)

user = input('Enter your function to draw: ')
plot(user)
