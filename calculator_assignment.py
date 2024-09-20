num1 = int(input("Number 1  "))
num2 = int(input("Number 2  "))
operation = input("Operator  ")


def add(num1,num2):
    return (num1 + num2)
if operation == "+":
    sum = add(num1,num2)
    print(sum)

def subtraction(num1,num2):
    return (num1 - num2)
if operation == "-":
    minus = subtraction(num1,num2)
    print(minus)

def multiply(num1,num2):
    return (num1 * num2)
if operation == "*":
    multiplication = multiply(num1,num2)
    print(multiplication)

def division(num1,num2):
    return (num1 / num2)
if operation == "/":
    divide = division(num1,num2) 
    print(divide) 