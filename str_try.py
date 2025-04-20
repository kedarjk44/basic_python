inp_str = "lenovoideapado"

op_dict = {}
for ch in inp_str:
    if ch in op_dict.keys():
        op_dict[ch] += 1
    else:
        op_dict[ch] = 1

print(op_dict)

op_lst = list(set(i for i in inp_str))
print(op_lst)

inp_lst = [1, 2, 1, 2]
print(list(set(inp_lst)))

lst1 = [1, 2, 3]
lst2 = lst1
lst2[1] = 5
print(lst1, lst2)


lst_try = [1,2,[3,4]]
print(lst_try)