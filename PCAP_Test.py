x = 3
y = 2
x = x % y
x = x % y
y = y % x
print(y)


list = [x*x for x in range(5)]
print(list)


def fun(lst):
    print(lst[2])
    print(lst[lst[2]])
    del lst[lst[2]]
    return lst


print(fun(list))

lst = [i for i in range(-1, -2)]
print(lst)

dct = {'one':'two', 'three':'one', 'two':'three'}
v = dct['three']

for k in range(len(dct)):
    v = dct[v]  # k is not used, only v is used
print(v)

tup = (1, 2, 4, 8)
tup = tup[-2:-1]  # second last and last element of tuple will be picked up
tup = tup[-1]
print(tup)

x, y = 2.0, 4.0
print(y ** (1/x))

x, y = "6", "3"
print(x+y)  # ---> since x and y are strings output will be string 63

nums = [1, 2, 3]
vals = nums  # ----> vals and nums point to the same list
print(vals)
del vals[:]
print(vals)
print(nums)


def func1(a):
    return None


def func2(a):
    return func1(a) * func1(a)

# print(func2(2)) -----------> Gives error since func1 returns None for everything

dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)
for x in dct.keys():
    print(dct[x][1], end="")


def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)


print()
print(fun(0, 3))

x = 1 // 5 + 1 / 5  # executed from right to left and both divisions are done first, (1/5 = 0.2)  + (1//5 = 0)
print(x)

print(1//2)  # this is integer division, result will be 0 and not 0.5

def func(a, b):
    return b ** a
# print(func(b=2, 2)) -------> Positional argument cannot follow keyword argument. Keyword arguments must be last


def test(inp=2, out=3):
    return inp*out


print(test(out=2))

x = 1
y = 2
x, y, z = x, x, y
print(x, y, z)
z, y, z = x, y, z
print(x, y, z)

print("a", "b", "c", sep="sep")

tup = (1, 2, 3, 4)
# tup[1] = tup[1] + tup[0] # -- > indicates that tuple is immutable

z = 0
y = 10
x = y < z and z > y or y > z and z < y
print(x)

lst = [[x for x in range(3)] for y in range(3)]
print(lst)
print(0 % 2, 1 % 2, 2 % 2)

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print(lst[r][c], end="")
            print("#")

lst = [1, 2]
for v in range(2):
    lst.insert(-1, lst[v])  # inserts at the beginning of the list, after 1st iteration of for loop list is [1, 1, 2] so for 2nd iteration 1 is inserted again
print(lst)  # makes the list 1, 1, 1, 2

a, b = 1, 0
a = a ^ b  # XOR operation
b = a ^ b
a = a ^ b
print(a, b)
