def toggle_characters(inp_word):
    out_word = ""
    for i in range(len(inp_word)):
        if inp_word[i] >= 'A' and inp_word[i] <= 'Z':
            out_word += (inp_word[i]).lower()
        elif inp_word[i] >= 'a' and inp_word[i] <= 'z':
            out_word += (inp_word[i]).upper()
        else:
            out_word += inp_word[i]
    print(out_word)


toggle_characters("TeSting*&*&")
