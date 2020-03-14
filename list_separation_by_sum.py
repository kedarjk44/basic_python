inp_arr1 = [20, 5, 6, 2, 14, 6]


def get_equal_sum_point(inp_arr):
    left_sum, right_sum = 0, 0
    for i in range(len(inp_arr)):
        j = len(inp_arr) - 1 - i
        left_sum += inp_arr[i]
        right_sum += inp_arr[j]
        print(left_sum, right_sum)
        if left_sum == right_sum and (i == len(inp_arr)//2 or j == len(inp_arr)//2):
            print(i, j)
        elif left_sum > right_sum:
            j += 1
            print(j)
        else:
            i -= 1
            print(i)


get_equal_sum_point(inp_arr1)