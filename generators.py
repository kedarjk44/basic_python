def generator(num):
    yield num+1
    yield num+2
    yield num+3


gen = generator(2)

print(gen.__next__(), end=" ")
print(gen.__next__(), end=" ")
print(gen.__next__(), "\n")
# outputs 3 4 5


def fib(a, b, limit):

    while a < limit:
        yield a

        a, b = b, a + b


x = fib(5, 6, 46)

print(x.__next__(), end=" ")
print(x.__next__(), end=" ")
print(x.__next__(), end=" ")
print(x.__next__(), end=" ")
print(x.__next__(), end=" ")
print(x.__next__(), end=" ")
# outputs 5 6 11 17 28 45
print("\n")


def gen():
    lst = range(5)
    for i in lst:
        yield i*i


for i in gen():
    print(i, end="")