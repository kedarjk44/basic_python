def list_reversal(inp_lst):
                return inp_lst[::-1]


print(list_reversal([1, 2, 3, 4]))


def string_palindrome(inp_str):
                return inp_str == inp_str[::-1]


print(string_palindrome("abcbda"))


def find_duplicates(data):
        """
        This function finds and prints duplicate elements in a list.
        Args: data: The list to check for duplicates.
        """
        # Use a set to store unique elements seen so far
        seen = set()
        duplicates = []
        for num in data:
                if num in seen:
                        duplicates.append(num)
                else:
                        seen.add(num)
        # Print the set of duplicates (if any)
        if duplicates:
                print("Duplicate elements in the list:", duplicates)
        else:
                print("No duplicates found in the list.")


# Example list with duplicates
my_data = [1, 2, 3, 4, 2, 7, 8, 1, 9]

find_duplicates(my_data)        # Output: Duplicate elements in the list: [2, 1]


def join_strings(string1, string2, separator=" "):
    """
    This function joins two strings with a specified separator.
    Args:   string1: The first string to join.
            string2: The second string to join.
            separator: The separator to insert between the strings (optional, defaults to space).
    Returns: The joined string.
    """
    # Join the strings using the separator
    joined_string = separator.join([string1, string2])
    return joined_string


# Example usage
str1 = "Hello"
str2 = "World"
combined_string = join_strings(str1, str2)
print(combined_string)    # Output: Hello World

# Join with a different separator
combined_string_with_dash = join_strings(str1, str2, separator="-")
print(combined_string_with_dash)    # Output: Hello-World

