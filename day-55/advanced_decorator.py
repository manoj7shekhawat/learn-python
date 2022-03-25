# Create the logging_decorator() function 👇

def logging_decorator(function):

    def wrapper(*args, **kwargs):
        print(f"You called: {function.__name__}({args[0]}, {args[1]}, {args[2]})")
        result = function(args[0], args[1], args[2])
        print(f"It returned: {result}")

    return wrapper


# Use the decorator 👇
@logging_decorator
def my_function(a, b, c):
    return a * b * c


my_function(1, 2, 3)