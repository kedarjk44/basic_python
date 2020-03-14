def binary_search(arr, target, low, high):
    if low > high:
        return False
    else:
        while low < high:
            mid = (low + high) // 2
            print(mid, high, low)
            if arr[mid] == target:
                return True
            elif target > arr[mid]:
                return binary_search(arr, target, mid + 1, high)
            elif target < arr[mid]:
                return binary_search(arr, target, low, mid - 1)
            return False


arr1 = [1, 2, 5, 7, 8, 9, 15, 17]
targ = 5
print(binary_search(arr1, targ, 0, len(arr1) -1))

data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 34, 37]
target = 5
print(binary_search(data, target, 0, len(data) - 1))