def string_combinations(inp_str):
    possible_strings = []    
    for i in range(len(inp_str),0,-1):
        new_str = ""
        for j in range(i):
            new_str = new_str + inp_str[j]
        if (new_str != ""):
            possible_strings.append(new_str)
    # print(possible_strings)
    return possible_strings


def string_splitter(inp_str):
    string_list = list(inp_str)
    word_list = []
    for i in range(len(inp_str)):
        new_str = ""
        for j in range(i,len(inp_str)):
            new_str = new_str + inp_str[j]
        if (new_str != "" and (len(new_str) > 1)):
            word_list.append(new_str)
    return word_list


def string_divider(inp_str):
    part1 = ""
    part2 = ""
    out_list = []
    print("Input string is: " + inp_str + str(int(len(inp_str)/2)))
    for i in range(int(len(inp_str) / 2)):
        part1 = part1 + inp_str[i]
        print(part1)
        part2 = part2 + inp_str[int(len(inp_str)/2) + i]
        print(part2)
    print("Part1 is: " + str(part1))
    print("Part2 is: " + str(part2))

    
def minion_game(inp_string):
    assert(len(inp_string) > 0)
    assert(len(inp_string) < 1000000)
    vowel_list = ['A','E','I','O','U']
    inp_alpha = []
    for alpha in inp_string:
        inp_alpha.append(alpha)

    set_alpha = set(inp_alpha)
    
    kevin_vowels = []
    stuart_cons = []

    split_strings = string_splitter(inp_string)
    words = []
    for string in split_strings:
        if (len(string) > 1):
            word_list = string_combinations(string)
        for word in word_list:
            words.append(word)

    for word in words:
        if ((word[0] in vowel_list) and (len(word) > 1)):
            kevin_vowels.append(word)
        elif ((word[0] not in vowel_list) and (len(word) > 1)):            
            stuart_cons.append(word)
    
    for alphabet in inp_alpha:
        if alphabet in vowel_list:
            kevin_vowels.append(alphabet)
        else:
            stuart_cons.append(alphabet)
    # print("Kevin: " + str(kevin_vowels) + str(len(kevin_vowels)))
    # print("\nStuart: " + str(stuart_cons) + str(len(stuart_cons)))
    
    if (len(kevin_vowels) > len(stuart_cons)):
        return ("Kevin " + str(len(kevin_vowels)))
    elif(len(kevin_vowels) < len(stuart_cons)):
        return ("Stuart " + str(len(stuart_cons)))
    elif (len(kevin_vowels) == len(stuart_cons)):
        return ("Draw")

inp_str = "BAANAANAASA"
print("This is output: " + str(minion_game(inp_str)))
string_divider(inp_str)
