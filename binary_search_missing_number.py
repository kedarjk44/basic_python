def find_missing_number(ar, N):
    low = 0
    high = N - 1
    while low <= high:
        mid = (low + high) // 2
        # mid = int(mid)
        # print(mid, high, low)
        print(ar[mid], ar[high], ar[low])
        # If this is the first element which is not index + 1, then missing element is mid+1
        if ar[mid] != mid + 1 and ar[mid - 1] == mid:
            return mid + 1
        # if this is not the first missing element search in left side
        elif ar[mid] != mid + 1:
            high = mid - 1
        # if it follows index+1 property then search in right side
        else:
            low = mid + 1
    # if no element is missing
    return -1


arr1 = [1, 2, 3, 4, 5, 7, 8, 9]
n = find_missing_number(arr1, len(arr1))
print(n)
