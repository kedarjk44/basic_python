# Generator Example
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1


counter = count_up_to(5)

print("\nGenerator Example:")
for num in counter:
    print(num)

# More complex generator example
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib_gen = fibonacci(10)

print("\nFibonacci Generator Example:")
for num in fib_gen:
    print(num)


# Closure Example
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function


closure_example = outer_function(10)
result = closure_example(5)

print("\nClosure Example:")
print("Result:", result)  # Output: 15


def multiplier(factor):
    def inner(number):
        return number * factor
    return inner


double = multiplier(2)
triple = multiplier(3)

print(double(5)) #prints 10
print(triple(5)) #prints 15