class testClass:
    __hiddenVariable = 0

    def addThis(self, add_inp):
        self.__hiddenVariable += add_inp
        return self.__hiddenVariable  # + add_inp

    def __hiddenMethod(self):
        print("Current value of hidden variable %d" % self.__hiddenVariable)

    def print_hidden(self):
        print("This public method will call the hidden method.")
        self.__hiddenMethod()


obj = testClass()
print(obj.__class__.addThis(obj, 6))  # ---> one of the ways to access methods

# print(obj.__hiddentVariable) ---------> This gives error

print(obj._testClass__hiddenVariable)  # ---> This works

print(obj.addThis(3))
print(obj.addThis(5))

print(obj._testClass__hiddenMethod()) # ---> This works

obj.print_hidden()