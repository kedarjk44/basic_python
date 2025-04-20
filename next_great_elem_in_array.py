def nextGreaterElement(arr):
    n = len(arr)
    result = [-1] * n  # Initialize result array with -1
    stack = []  # Stack to store indices of elements

    for i in range(n):
        # Pop elements from stack while they are smaller than the current element
        while stack and arr[i] > arr[stack[-1]]:
            result[stack.pop()] = arr[i]
        # Push the current element's index onto the stack
        stack.append(i)
    return result


# Example usage
# arr = [4, 5, 2, 25]
arr = [13, 7, 6, 12]
output = nextGreaterElement(arr)

for i, val in enumerate(arr):
    print(f"{val} --> {output[i]}")
