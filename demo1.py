def greet():
    print("HELLO SANJIVANI")
greet()

def exc(func):
    func()
    exc(greet)
    
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def mod(x, y):
    return x % y

def exponent(x, y):
    return x ** y


def perform_operation(operation,a,b):
    return operation(a,b)
result=perform_operation(add,10,4)

def perform_operation(operation,x,y):
    return operation(x,y)
result1=perform_operation(sub,10,4)
print(result1)
def square(a):
    return a*a
def compose(f,g):return lambda x,y:f(g(x,y))
result=compose(square,add)(2,3)
print(result)

operations={'+':add, '-':sub, '*':mul, '/':div}

operator=input("Enter an operator(+,-,*,/):")
a =float(input("Enter the 1st number:"))

b =float(input("Enter the 2nd number:"))

if operator in operations:
    result=operations[operator](a,b)
    print("Result:",result)
else:
    print("Invalid operator")
    
def outer_func():
    def inner_func():
        print("Hello, World!")    
    inner_func()


