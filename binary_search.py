def linear_search(data, target):
    for i in range(len(data)):
        if target == data[i]:
            return True
    return False


def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (high+low) // 2
        print(1, mid, high, low)
        if data[mid] == target:
            # print(2, mid, high, low)
            return True
        elif target < data[mid]:
            # print(3, mid, high, low)
            high = mid - 1
            # print(4, mid, high, low)
        else:
            # print(5, mid, high, low)
            low = mid + 1
            # print(6, mid, high, low)
    return False


def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (high + low) // 2
        # print(mid, low, high)
        if target == data[mid]:
            return True
        elif target > data[mid]:
            return binary_search_recursive(data, target, mid+1, high)
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid-1)
        return False


data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 34, 37]
target = 5

print(binary_search_recursive(data, target, 0, len(data)-1))
# print(binary_search_iterative(data, target))

