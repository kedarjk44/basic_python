# Write a program to convert first letter of firstname and first letter of lastname #to upper case.

inp_lst = ['abby.sia@testskope.com', 'abby.saldivia@testskope.com', 'adabalaRavi.kumar@testskope.com']
#abegail.delacruz@testskope.com
#adabalaRavi.kumar@testskope.com
#alan.yeung@testskope.com
#robertson.alan@testskope.com
#Aldwen.Laspoa@testskope.com

for inp in inp_lst:
    new_inp = inp.split('@')
    # print(new_inp[0], new_inp[1])
    out_str = ""
    for new in new_inp[0].split('.'):
        # print(new.capitalize())
        if out_str == "":
            out_str += new.capitalize()
        else:
            out_str = out_str + "." + new.capitalize()
    # print(out_str.strip("."))
    # print(out_str.lstrip("."))
    out_str = out_str + "@" + new_inp[1]
    print(out_str)

# print("hello world")

inp = "My #name is$ Kedar"
# op= "Kedar #is name$ My"

# - 3
#$ - 8


def rev_inp_str(inp_str):
    str_lst = inp_str.split(" ")
    # print(str_lst)
    new_str = []
    # special_char_list = ['#', '$']
    for i in range(len(str_lst)-1, -1, -1):
        new_str.append(str_lst[i])
    # print(new_str)
    op_str = " ".join(new_str)
    return op_str


op_str = rev_inp_str(inp)

print(op_str)