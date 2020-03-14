
class test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "this is repr method, %d and %d" % (self.a, self.b)

    def __str__(self):
        return "this is str method, %d and %d" % (self.a, self.b)


newobj = test(15, 20)
print(newobj)  # ---> this calls __str__ method
print([newobj])  # ---> this calls __repr__ method
