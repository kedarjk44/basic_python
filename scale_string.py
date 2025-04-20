# Scale the strings Create below output
#  Input = "abcd"
#  Output ="a-bb-ccc-dddd"

def scale_strings(inp_str):
    new_str = ""
    for i in range(len(inp_str)):
        new_str += inp_str[i] * (i+1) + "-"
    return new_str


inp_str = "abcd"

print(scale_strings(inp_str).strip("-"))
