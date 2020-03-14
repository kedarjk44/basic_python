from Stack import Stack


def rev_string(inp_str):
    s = Stack.Stack()
    for i in range(len(inp_str)):
        s.push(inp_str[i])

    rev_str = ""
    while not s.is_empty():
        rev_str += s.pop()
    return rev_str


print(rev_string("goffog"))

test_str = "this is a string"
print(test_str[::-1])
print(test_str[0::1])  # will print the string as it is
test2 = "AQUAFINAN"
new_dict = {}
for i in range(len(test2)):
    if test2[i] in list(new_dict.keys()):
        new_dict[test2[i]] += 1
    else:
        new_dict[test2[i]] = 1

print(new_dict)
for k, v in new_dict.items():
    print("Number of %s are %s." % (k, v))

test2_list = list(dict.fromkeys(test2))  # Removes the duplicates from list or string
print(test2_list)

test3 = "this is a test3"
test4 = test3.replace("is", "was")
print(test4)
print(isinstance(test4, str))
