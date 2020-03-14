def binary_search_recursive(data, target, high, low):
    print(high, low)
    if high < low:
        return -1
    else:
        mid = (high + low) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
            return binary_search_recursive(data, target, high, low)
        elif data[mid] > target:
            high = mid - 1
            return binary_search_recursive(data, target, high, low)


def count_occurrences(data, index, target):
    if index == -1:
        return 0
    count = 1
    left = index - 1
    # right = len(data) - 1
    while data[left] == target and left >= 0:
        count += 1
        left -= 1
    right = index + 1
    while right <= len(data) - 1 and data[right] == target:
        count += 1
        right += 1
    return count


data2 = [2, 4, 5, 5, 5, 5, 5, 6, 7, 8, 9, 27, 27, 27, 34, 37]
target2 = 27
index = binary_search_recursive(data2, target2, len(data2) - 1, 0)
print(index)
count = count_occurrences(data2, index, target2)
print(count)

# binary_search_count_occurrence_recursive(data2, target2, 0, len(data2) - 1, 0)

