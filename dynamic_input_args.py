def dynamic_arguments(*args, **kwargs):
    """
    A function that accepts dynamic arguments using *args and **kwargs.

    *args: Accepts any number of positional arguments as a tuple.
    **kwargs: Accepts any number of keyword arguments as a dictionary.
    """

    print("Positional arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage:
dynamic_arguments(1, 2, "hello", 3.14, name="Alice", age=30, city="New York")

dynamic_arguments("only one positional arg")

dynamic_arguments(key1 = "val1", key2 = 2, key3 = True)

dynamic_arguments() # calling with no arguments.