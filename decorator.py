def print_return(func):
    def print_output(*args, **kwargs):
        x = func(*args, **kwargs)
        print(x)
        return print_return(*args, **kwargs)
    return print_output


def add_star(func):
    def inner(*args, **kwargs):
        print("*"*30)
        func(*args, **kwargs)
        print("*" * 30)
        return add_star(*args, **kwargs)
    return inner


@add_star
@print_return
def simple_func(inp_string):
    return inp_string + " anything to add"


simple_func("this is test")
add_star(print_return(simple_func("xyz")))
