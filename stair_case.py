def stair_cases(inp_num):
    for i in range(inp_num+1, 0, -1):
        print(' ' * (inp_num-i), end="")
        print('*' * (inp_num+1-i))


stair_cases(5)


def newstair_cases(inp_num):
    # i, j = None, None
    print(' ' * inp_num + '*')
    for i in range(inp_num+1, -1, -1):
        print(' ' * i, end="")
        print('*' * (inp_num+1-i), end="")
        print('*' * (inp_num + 1 - i))


newstair_cases(5)
