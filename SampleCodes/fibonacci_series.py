a, b = 0, 1
for x in range(10):
    a, b = b, a+b
    print(a, end=" ")

print()


def fib(n):
    a, b = 0, 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            a, b = b, a+b
            yield a+b


print(list(fib(10)))
