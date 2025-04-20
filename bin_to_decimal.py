def binary_to_decimal_custom(binary):
    decimal = 0
    base = 1  # Represents 2^0 initially

    # Iterate through the binary string from right to left
    for digit in reversed(binary):
        if digit == '1':
            decimal += base
        base *= 2  # Multiply base by 2 for each position

    return decimal

# Example usage:
binary_str = "1100"
print(binary_to_decimal_custom(binary_str))  # Output: 12


def decimal_to_binary_recursive(num):
    if num == 0:
        return "0"  # Special case for decimal 0
    elif num == 1:
        return "1"
    else:
        return decimal_to_binary_recursive(num // 2) + str(num % 2)


def add_two_bin_nums(a, b):
    dec_a = binary_to_decimal_custom(a)
    print(dec_a)
    dec_b = binary_to_decimal_custom(b)
    print(dec_b)
    sum_of_ab = dec_a + dec_b

    bin_sum = decimal_to_binary_recursive(sum_of_ab)
    return bin_sum


bin_a = "1000"
bin_b = "111"

print(add_two_bin_nums(bin_a, bin_b))



