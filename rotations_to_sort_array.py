def countRotations(arr):
    min_val = arr[0]
    min_index = 0
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            min_index = i
    return min_index


def countRotations2(arr):
    count = 1
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return count
        else:
            count += 1


arr = [3, 4, 8, 9, 1, 2]
# n = len(arr)
print("Number of rotations:", countRotations2(arr))


# using binary search
def find_rotation_count(arr):
    low = 0
    high = len(arr) - 1
    n = len(arr)
    while low <= high:
        if arr[low] <= arr[high]:
            return low
        mid = (low + high) // 2
        next_mid = (mid + 1) % n
        prev_mid = (mid + n - 1) % n
        if arr[mid] <= arr[next_mid] and arr[mid] <= arr[prev_mid]:
            return mid
        elif arr[mid] <= arr[high]:
            high = mid - 1
        else:
            low = mid + 1


arr = [3, 4, 5, 6, 8, 10, 1, 2]
print("Rotation count:", find_rotation_count(arr))
