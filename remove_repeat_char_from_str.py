def trim_repetitives(data):
    """
    This function removes consecutive repetitions of characters from a string.
    Args: data: The string to be processed.
    Returns: A new string with consecutive repetitions removed.
    """
    # Initialize an empty string to store the result
    result = ""
    # Iterate through the input string
    prev_char = None
    for char in data:
        # Append the character if it's different from the previous one
        if char != prev_char:
            result += char
        prev_char = char
    return result


# Example usage
input_string = "aaabbbbvdcccddd"
trimmed_string = trim_repetitives(input_string)
print(trimmed_string)    # Output: abcd
