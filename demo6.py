def divide_numbers(x,y):
    if y==0:
        raise ZeroDivisionError("Cannot divide by zero!")
    else:
        return x/y
    
try:
    result = divide_numbers(10,5)
    print(int(result))

except ZeroDivisionError as error:
    print("Error:",str(error))