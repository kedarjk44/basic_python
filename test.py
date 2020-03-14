# m = 20
# l = 6
#
# print(m//l, m/l, m%l)
#
# fh = open("D:\Buildbot_Carbonite_upload_log.txt", 'r')
#
# print(fh.read())


class dog:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class bulldog(dog):
    def __init__(self, name, has_fur):
        super(bulldog, self).__init__(name)
        self.fur = has_fur

    def check_fur(self):
        return self.fur


class big_bulldog(bulldog):
    def __init__(self, name, has_fur, colour):
        super(big_bulldog, self).__init__(name, has_fur)
        self.colour = colour

    def get_colour(self):
        return self.colour


bd = bulldog("bd1", True)
print(bd.get_name())
print(bd.check_fur())

bd2 = big_bulldog("bd2", False, "Black")
print(bd2.check_fur())
print(bd2.get_colour())


i = 5
while i>0:
    i=i//2
    print(i)
    if i%2 == 0:
        break
else:
    i+=1
print("here", i)

for i in range(1,3):
    print("1", end="")
else:
    print("x")

print(3423e-2)
print(.3423e2)

a = [0]
b=a[:]
a[0]=1
print(a, b)

test_str = "abcdefgh"
print(test_str[1:-2])
