def find_pairs_bruteforce(arr, k):
    result = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == k and (arr[i], arr[j]) not in result:
                result.append((arr[i], arr[j]))
    return result


arr = [5, 6, 5, 7, 4, 7, 3, 5, 2, 8]
k = 10
result_bruteforce = find_pairs_bruteforce(arr, k)
print(result_bruteforce)
# print(list(set(result_bruteforce)))  # Output: [(5, 5), (6, 4), (7,3)]
