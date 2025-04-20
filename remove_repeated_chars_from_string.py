inp_str = "aabbbbccccccccccddddddaaadddeeeffffffee"
op_str = ""
for i in range(len(inp_str)):
    if inp_str[i] in op_str:
        if inp_str[i] != op_str[-1]:
            op_str = op_str + inp_str[i]
        else:
            continue
    else:
        op_str = op_str + inp_str[i]

print(op_str)

# str1 = "abcd"
# str1[2] = "p" # TypeError: 'str' object does not support item assignment
# print(str1)