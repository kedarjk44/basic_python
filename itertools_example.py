from itertools import combinations, permutations


def main():
    input_list = ['k', 'e', 'd', 'a', 'r']

    # output_list = list(combinations(input_list, 3))
    # print("Combinations ", output_list)  # Output as list of tuples
    # perm_output = []
    # for i in range(len(output_list)):
    #     perm_output.append(list(output_list[i]))
    #
    # print("\n Permutations output: ", perm_output)  # Output as list of lists
    # for i in range(len(perm_output)):
    #     print()

    output2 = list(permutations(input_list, 3))
    print("\n Permutations list: ", output2)  # Output as list of tuples
    list_output = []
    for i in range(len(output2)):
        list_output.append(list(output2[i]))

    print("\n", list_output)  # Output as list of lists


main()
