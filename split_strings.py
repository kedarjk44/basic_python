def splitter(inp_str):
    splt = inp_str.split("-")
    splt.remove(splt[-1])
    splt.remove(splt[-1])
    print(splt)
    return "-".join(splt)


def main():
    # str1 = "audit-123h324h-ertrt"
    # str2 = "audit-taskrunner-1234dfsgfdg-yrty345"
    # op_str1 = splitter(str1)
    # print(op_str1)
    # op_str2 = splitter(str2)
    # print(op_str2)
    inp_str = "abc de f"
    space_position = []
    for i in range(len(inp_str)):
        if inp_str[i] == " ":
            space_position.append(i)
    print(space_position)

    op_str = ""
    for i in range(len(inp_str[::-1])):
        if inp_str[::-1][i] != " ":
            op_str = op_str + inp_str[::-1][i]
    print(op_str)
    new_op_str = ""
    for i in range(len(op_str)):
        if i == space_position[0]:
            new_op_str = op_str[0:i:] + " "
            space_position.pop(0)
    print(new_op_str)


if __name__ == "__main__":
    main()