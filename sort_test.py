import datetime


def sort_list(inp_list):
    start_time = datetime.datetime.now().microsecond
    print(datetime.datetime.now())
    for i in range(len(inp_list)):
        for j in range(len(inp_list)-1):
            if inp_list[j] > inp_list[j+1]:
                inp_list[j], inp_list[j+1] = inp_list[j+1], inp_list[j]
    total_time = datetime.datetime.now().microsecond - start_time
    print(datetime.datetime.now())
    print(inp_list)


def while_sort(inp_list):
    start_time = datetime.datetime.now().microsecond
    print(datetime.datetime.now())
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(inp_list)-1):
            if inp_list[i] > inp_list[i+1]:
                swapped = True
                inp_list[i], inp_list[i+1] = inp_list[i+1], inp_list[i]
    total_time = datetime.datetime.now().microsecond - start_time
    print(datetime.datetime.now())
    print(inp_list)


lst1 = [12, 13, 98, 5, 6, 23, 25, 1, 56, 72, 10, 12, 13, 98, 5, 6, 230, 205, 1, 565, 722, 108]
sort_list(lst1)
while_sort(lst1)
