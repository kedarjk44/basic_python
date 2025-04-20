def check_balance(inp_str):
    count = 0
    for char in inp_str:
        if char == "(":
            if count >= 0:
                count += 1
            else:
                return False
        else:
            count -= 1
    if count:
        print(count)
        return False
    else:
        print(count)
        return True


paran_str = "()(((())))(())((()))"
print(check_balance(paran_str))
