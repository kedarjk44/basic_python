def decimal_to_binary_recursive(num):
    if num == 0:
        return "0"  # Special case for decimal 0
    elif num == 1:
        return "1"
    else:
        return decimal_to_binary_recursive(num // 2) + str(num % 2)


# Example usage:
decimal_val = 8
binary_result = decimal_to_binary_recursive(decimal_val)
print(binary_result)  # Output: "11000"
