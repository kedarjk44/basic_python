
def duplicate_vowels(inp_word):
    out_word = ""
    for i in range(len(inp_word)):
        if (inp_word[i]).upper() in ['A', 'E', 'I', 'O', 'U']:
            out_word += inp_word[i] * 2
        else:
            out_word += inp_word[i]

    print(out_word)


duplicate_vowels("Python")
duplicate_vowels("JAVA")
duplicate_vowels("this is a test string")
