from Stack import Stack


def div_by_2(dec_num):
    if dec_num == 0:
        return 0
    s = []  # Stack.Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.append(remainder)
        dec_num = dec_num // 2

    bin_num = ""
    while not s == []:  # s.is_empty():
        bin_num += str(s.pop())

    return bin_num


print(div_by_2(142))
print(div_by_2(143))

data = [2, 4, 68, 65, 48, 77, 99]

if 77 in data:
    print("yes")