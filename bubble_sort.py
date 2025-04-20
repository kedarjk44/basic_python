def bubble_sort(data):
    """
    Sorts a list of data in ascending order using the bubble sort algorithm.
    Args:
            data: The list to be sorted.
    Returns:
            A new list containing the sorted data.
    """
    # Loop through the list n-1 times
    for i in range(len(data) - 1):
        # Swap adjacent elements if they are in the wrong order
        for j in range(len(data) - i - 1):
            # print(i, j)
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    # Return the sorted list (new list is created)
    return data.copy()


# Example usage
my_data = [64, 34, 25, 12, 22, 22, 11, 90, 18]
sorted_data = bubble_sort(my_data)    # Copy the list to avoid modifying the original
print(sorted_data)    # Output: [11, 12, 22, 25, 34, 64, 90]
