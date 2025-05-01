# My #Name is $Kedar
# Kedar #is Name $My

inp_str = "My full #Name is $Kedar @Kulkarni"

special_chars = ['@', '#', '$', '%', '&', '*', '!', '^', '(', ')', '-', '=', '+', '_', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']

op_lst = inp_str.split(" ")
# print(op_lst)
index_lst = {}
for i in range(len(op_lst)):
    # print(op_lst[i])
    if str(op_lst[i][0]) in special_chars:
        index_lst[i] = op_lst[i][0]

print(index_lst)
op_str = ""
op_lst = op_lst[::-1]

for i in range(len(op_lst)):
    append_item = op_lst[i].lstrip("".join(special_chars))
    # print(append_item)
    if i in list(index_lst.keys()):
        append_item = index_lst[i] + append_item
        # print(append_item)
        op_str = op_str + " " + append_item
    else:
        op_str = op_str + " " + append_item

print(op_str.strip())