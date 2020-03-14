def capitalize(string):
    words_in_string = string.split(" ")
    op_str = ""
    for word in words_in_string:
        word = word.capitalize()
        print(word)		
        op_str = op_str + word + " "
    return op_str


new_str = capitalize("hello world")
print(new_str)
cap_str = "this is not capitalized"
print(cap_str.capitalize())
print(*[x.capitalize() for x in list(cap_str)])