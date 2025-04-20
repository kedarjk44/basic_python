def binary_search(arr, target):
    """
    Performs binary search on a sorted array.

    Args:
        arr: The sorted array to search.
        target: The value to search for.

    Returns:
        The index of the target if found, otherwise -1.
    """

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Integer division to find the middle index

        if arr[mid] == target:
            return mid  # Target found, return its index
        elif arr[mid] < target:
            low = mid + 1  # Target is in the right half
        else:
            high = mid - 1  # Target is in the left half

    return -1  # Target not found


# Example usage:
sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_value = 23

result = binary_search(sorted_list, target_value)

if result != -1:
    print(f"Target {target_value} found at index {result}")
else:
    print(f"Target {target_value} not found in the list")

target_value2 = 40
result2 = binary_search(sorted_list, target_value2)

if result2 != -1:
    print(f"Target {target_value2} found at index {result2}")
else:
    print(f"Target {target_value2} not found in the list")