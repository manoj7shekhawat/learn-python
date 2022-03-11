# Var agrs
def add(*args):
    total = 0
    for n in args:
        total += n

    return total


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# Kewords arguments
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(2, add=3, multiply=5))
