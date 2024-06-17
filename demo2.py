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

def perform_operation(operation,a,b):
    return operation(a,b)
result=perform_operation(add,10,4)

print(result)
result=perform_operation(sub,10,4)

print(result)
def square(a):
    return a*a
def compose(f,g):return lambda x,y:f(g(x,y))
result=compose(square,add)(2,3)

print(result)
