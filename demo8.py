def add_decorator(func):
    def wrapper(a, b):
        print("Before: Something is Happening!!")
        result = func(a, b)
        print("After: Something is Happening!!")
        return result
    return wrapper

@add_decorator
def add_numbers(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}")
    return result

result = add_numbers(3, 5)



