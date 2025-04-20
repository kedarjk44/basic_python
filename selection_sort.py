def selection_sort(data):
  """
  Sorts a list of data in ascending order using the selection sort algorithm.
  Args:      data: The list to be sorted.
  Returns:    A new list containing the sorted data.
  """
  for i in range(len(data)):
    # Find the minimum element in the unsorted part
    min_index = i
    for j in range(i + 1, len(data)):
      if data[j] < data[min_index]:
        min_index = j
    # Swap the found minimum element with the first element of the unsorted part
    if i != min_index:
      data[i], data[min_index] = data[min_index], data[i]
  # Return the sorted list (new list is created)
  return data.copy()

# Example usage
my_data = [64, 34, 25, 12, 22, 11, 90]
sorted_data = selection_sort(my_data)  # Copy the list to avoid modifying the original
print(sorted_data)  # Output: [11, 12, 22, 25, 34, 64, 90]
