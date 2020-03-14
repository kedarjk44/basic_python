movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}

def sort_last(tuples):
  my_dict = {}
  last_items = []
  for my_tuple in tuples:
    last_items.append(my_tuple[len(my_tuple)-1])
    my_dict[my_tuple[len(my_tuple)-1]] = my_tuple
    last_items.sort()
    print(my_dict)
    print("%s" %last_items)
    sorted_items = []
    for key in last_items:
      sorted_items.append(my_dict[key])
    print("%s " %sorted_items)	
    return sorted_items


print(*movies.items())


def front_back(a, b):
    # +++your code here+++
    new_str = a[:int(len(a)/2)]+b[:int(len(b)/2)] + a[int(len(a)/2):len(a)]+b[int(len(b)/2):len(b)]
    print("%s" %new_str)
    return new_str


garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled [len(garbled)+1::-2]
print(*message)

tuples = ([(1, 3), (3, 2), (2, 1)])
sort_last(tuples)
front_back('abcd', 'xy')

