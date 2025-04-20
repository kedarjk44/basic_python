
def rotate_left(arr, k):
    return arr[k:] + arr[:k]


def rotate_right(arr, k):
    return arr[-k:] + arr[:-k]


arr = [1, 2, 3, 4, 5]
k = 3  # Number of positions to rotate

left_rotated = rotate_left(arr, k)
right_rotated = rotate_right(arr, k)

print("Left rotation:", left_rotated)  # Output 1
print("Right rotation:", right_rotated)  # Output 2

