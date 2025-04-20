import copy

# Shallow Copy Example
original_list = [1, 2, [3, 4]]
shallow_copy = copy.copy(original_list)

print("Original:", original_list)
print("Shallow:", shallow_copy)

original_list[2][0] = 5  # Modify a nested list

print("\nAfter modification:")
print("Original:", original_list)
print("Shallow:", shallow_copy)  # Shallow copy reflects the change

# Deep Copy Example
original_list = [1, 2, [3, 4]]
deep_copy = copy.deepcopy(original_list)

print("\nOriginal:", original_list)
print("Deep:", deep_copy)

original_list[2][0] = 5  # Modify a nested list

print("\nAfter modification:")
print("Original:", original_list)
print("Deep:", deep_copy)  # Deep copy remains unchanged
