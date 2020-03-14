from itertools import combinations


def get_palindromes(inp_string):
    str_combinations = combinations(inp_string, sub_string_length)
    str_list = list(str_combinations)
    list_of_palindromes = []
    for i in range(len(str_list)):
        # list_of_strings.append("".join(str_list[i]))
        new_str = "".join(str_list[i])
        if new_str == new_str[::-1]:
            list_of_palindromes.append(new_str)
    print(list_of_palindromes)


def count_substring(string, sub_string):
    start_index = string.find(sub_string)
    count = 0
    for i in range(start_index, len(string)):
        # print(string[i:(i+len(sub_string))])

        if sub_string == string[i:(i+len(sub_string))]:
            count = count + 1
    return count


if __name__ == '__main__':
    string = "maaadaaam maaadaaam"  # input("Enter the string: ").strip()
    sub_string_length = 10  # input("Enter the substring to search: ").strip()
    get_palindromes(string)
    
    # count = count_substring(string, sub_string)
    # print(count)

