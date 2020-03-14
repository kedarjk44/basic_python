import math
print(dir(math))

# class Candies:
#     @staticmethod
# def count_candies(starting_amount, new_every):
#     count = 0
#     while starting_amount > 0:
#         temp = starting_amount - new_every
#         if temp < 0:
#             count += starting_amount
#             break
#         else:
#             count += new_every
#         starting_amount = temp + 1
#
#     return count
#
# print(count_candies(7, 2))

# tup = (1, 4, (34, 14, 36, 58))
# for i in range(len(tup[2])):
#     print(tup[2][1:3])
# print(tup(2)[1:3])


def tuple_slice(startIndex, endIndex, tup):
    tmp_list = []
    for i in range(endIndex - startIndex):
        tmp_list.append(tup[i+1])
    print(tmp_list)
    out_str = ""
    for i in range(len(tmp_list)):
        out_str += str(tmp_list[i]) + ","
    return out_str.strip(",")


print(tuple_slice(1, 4, (76, 34, 13, 64, 12)))


def nth_most_rare(elements, n):
    tmp_dict = {}
    for elm in elements:
        if elm in tmp_dict.keys():
            tmp_dict[elm] = tmp_dict[elm] + 1
        else:
            tmp_dict[elm] = 1
    print("tmp", tmp_dict)
    new_dict = {k: v for k, v in sorted(tmp_dict.items(), key=lambda item: item[1])}
    print("new", new_dict)
    key_list = list(new_dict.keys())
    # print(key_list)
    # rev_key_list = [elm for elm in reversed(key_list)]
    # print("reversed", rev_key_list)
    # print(rev_key_list[n-1])
    print(key_list[n-1])
    # print(new_dict[2])
    # for k, val in tmp_dict.items():
    #     if n == val:
    #         return k



# print(nth_most_rare([5, 5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2))

print(nth_most_rare(["a", "a", "b", "c", "d", "e", "a", "b", "c", "d", "a", "b", "c", "a", "b", "a"], 2))




