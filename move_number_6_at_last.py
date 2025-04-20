def remove_non_six_elements(arr):
    # Remove non-six elements from the front
    new_arr = []
    num_6_count = 0
    for i in range(len(arr)):
        if arr[i] != 6:
            new_arr.append(arr[i])
        else:
            num_6_count += 1

    return new_arr, num_6_count


arr = [7, 6, 4, 6, 9, 6, 2, 6, 1, 6, 6, 6, 7, 6]
result, num_6_count = remove_non_six_elements(arr)
for i in range(num_6_count):
    result.append(6)
print(result)  # Output: [7, 4, 9, 2, 1, 7, 6, 6, 6, 6, 6, 6, 6]


def move_6_at_last(arr):
    counter = 0
    for i in range(len(arr)):
        if arr[i] == 6:
            arr.pop(i)
            arr.append(6)

    return arr


print(move_6_at_last(arr))