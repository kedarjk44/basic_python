from time import sleep


inp_str = "My name is kedar"
op_lst = inp_str.split(" ")
print(op_lst)
# print(op_lst[::-1], inp_str[::-1])
op_str = []

for i in range(len(op_lst)-1, -1, -1):
    print(op_lst[i])
    op_str.append(op_lst[i])

print(op_str)
new_op_str = " ".join(op_str)
print(new_op_str)

palindrome_chk = "rotator"
if palindrome_chk == palindrome_chk[::-1]:
    print("yes")

inp_arr = [1, 2, 3, 2, 4, 5, 1]
out_dict = {}
for i in range(len(inp_arr)):
    if inp_arr[i] in list(out_dict.keys()):
        out_dict[inp_arr[i]] += 1
    else:
        out_dict[inp_arr[i]] = 1

print(out_dict)
out_lst = []
for k,v in out_dict.items():
    print(k,v)
    if v > 1:
        out_lst.append(k)

print(out_lst)

inp_ar1 = [1, 2, 4, 5, 6, 8]
n = 5
i = 0
while i < n and i < len(inp_ar1)+1:
    if inp_ar1[i+1] == inp_ar1[i] + 1:
        i = i + 1
    else:
        print("missing %d" %(inp_ar1[i]+1))
        i = i + 1
        continue


def add_star(inp_func):
    def sub_func(*args, **kwargs):
        print('***************')
        result = inp_func(*args, **kwargs)
        print('***************')
        return result
    return sub_func


def add_logger_time(inp_func):
    def sub_func(*args, **kwargs):
        print(f"Function called: {inp_func.__name__}")
        return inp_func(*args, **kwargs)
        # print("Function ended")
        # return result
    return sub_func
@add_logger_time
@add_star
def print_inp_name(name):
    # sleep(2)
    print("Hi %s" % name)
    # sleep(2)


print_inp_name("Kedar")




