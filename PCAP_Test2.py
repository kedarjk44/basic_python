class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration

        v = self.s[self.i]
        self.i += 1
        return v


for x in I():
    print(x, end="")

print()


def I(n):
    s = '+'
    for i in range(n):
        s += s
        yield s


for x in I(2):
    print(x, end='')