# Remove adjacent duplicates form string
# Input : aaabbbbccccabc
# Output : abcabc

def remove_adjacent_duplicates_stack(s):
    stack = []
    for char in s:
        if not stack or stack[-1] != char:
            stack.append(char)
    return ''.join(stack)


input_str = "aaabbbbccccabc"
output_str = remove_adjacent_duplicates_stack(input_str)
print(output_str)  # Output: "abcabc"
