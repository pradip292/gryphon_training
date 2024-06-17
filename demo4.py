def greet(name="INDIA", age=60):
    print("Hello, " + name+"! You are",age,"years old")
    
greet(name="Vaishnavi", age=20)

greet(name="Shruti", age=21)

greet(age=20)

greet("INDIA")

greet("INDIA",age=30)

global_var=99
print("global_var",global_var)
def var():
    global global_var
    global_var=100
    print("global_var",name=global_var)

