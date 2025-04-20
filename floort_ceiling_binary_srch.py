# Given a sorted array and a value x, the ceiling of x is the smallest element in array greater than  to x,
# and the floor is the greatest element smaller than  to x.
# Assume than the array is sorted in non-decreasing order. Write efficient functions to find floor and ceiling of x.
# eg:
# [2,8,10,16,34]
# ceiling(10) = 16
# floor(10) = 8

def ceiling(arr, x):
    low, high = arr.index(x), len(arr) - 1

    # If x is greater than the last element, return the last element
    if x >= arr[high]:
        return arr[high]

    while low <= high:
        # mid = low + (high - low) // 2
        mid = (low + high) // 2
        if arr[mid] == x:
            return arr[mid+1]
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    # If we reach here, x lies between arr[i] and arr[i+1]
    return arr[low]


def floor(arr, x):
    low, high = 0, arr.index(x) #x #len(arr) - 1

    # If x is smaller than or equal to the first element, return the first element
    if x <= arr[low]:
        return arr[low]

    while low <= high:
        #mid = low + (high - low) // 2
        mid = (low + high) // 2
        if arr[mid] == x:
            return arr[mid-1]
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    # If we reach here, x lies between arr[i] and arr[i+1]
    return arr[high]


# Example usage
arr = [2, 8, 10, 16, 34]
x = 10
print("Floor of", x, "is", floor(arr, x))  # Output: 8

print("Ceiling of", x, "is", ceiling(arr, x))  # Output: 16

