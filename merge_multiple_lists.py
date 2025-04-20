inp_lst = [[1, 7, 11], [2, 8, 12], [4, 9, 13], [5, 10, 14], [6,11,16]]
op_lst = []

for j in range(len(inp_lst)):
    for i in range(len(inp_lst)):
        if inp_lst[i]:
            op_lst.append(min(inp_lst[i]))
            inp_lst[i].remove(min(inp_lst[i]))
            print(inp_lst)
print(op_lst)
