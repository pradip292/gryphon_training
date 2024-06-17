class UndefinedError(Exception):
    pass

def divide_numbers(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    else:
        return x / y

try:
   
    result = divide_numbers(10,0)
    print(int(result))

except ZeroDivisionError as error:
    print("Error Occurred!!")
    print("The Error is Caught ZeroDivisionError:", str(error))

except UndefinedError as error:
    print("Error Occurred!!")
    print("The Error is Caught UndefinedError:", str(error))

except Exception as error:
    print("Error Occurred!!")
    print("The error is Caught generic Exception:", str(error))
