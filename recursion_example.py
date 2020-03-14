# Code to calculate factorial
def factorial(inp_num):
    if inp_num <= 0:
        print("Enter a number more than 0")
    elif inp_num == 1:
        return 1
    else:
        return inp_num * factorial(inp_num-1)


x = factorial(-5)
print(x)
