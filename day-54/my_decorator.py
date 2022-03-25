import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(func_name):

    def wrapper_function():
        func_name()
        now_time = time.time()
        print(f"{func_name.__name__} run speed: {now_time - current_time}")
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
