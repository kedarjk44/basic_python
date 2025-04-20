def solution(digits):
    # Convert the digits list to an integer
    num = int("".join(map(str, digits)))
    # Increment the integer by 1
    num += 1
    # Convert the incremented integer back to a list of digits
    result = [int(digit) for digit in str(num)]
    return result


# Example usage
digits1 = [1, 2, 3]
digits2 = [1, 2, 9]
digits3 = [9, 9, 9]

print(solution(digits1))  # Output: [1, 2, 4]
print(solution(digits2))  # Output: [1, 3, 0]
print(solution(digits3))  # Output: [1, 0, 0, 0]
