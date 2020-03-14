# lambda can be used instead of writing a function
add_two_inputs = lambda x, y: x + y

print(add_two_inputs(8, 5))
print(add_two_inputs("this", " that"))

# map can be used to apply a function to each element of a list
list1 = [1, 2, 3, 4]
print(*list(map(lambda x: x**2, list1)))
# or can be done as
print(*[x**2 for x in list1])

# filter can be used to apply a condition to list
print(*list(filter(lambda x: x > 2, list1)))
# or can be done as
print(*[x for x in list1 if x > 2])

