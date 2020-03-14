def insert_in_list(my_list, position, value):
    return my_list.insert(position, value)


def append_in_list(my_list, value):
    return my_list.append(value)


def remove_from_list(my_list, rvalue):
    print(my_list, rvalue)
    new_list = [x for x in my_list if (x != rvalue)]
    print(new_list)
    return new_list


def pop_from_list(my_list):
    return my_list.pop()


def print_list(my_list):
    print(my_list)


def reverse_list(my_list):
    return my_list.reverse()


def main():
    N = int(input())
    my_list = []
    for i in range(N):
        i_read = input()
        # print(i_read)
        command = i_read.split(" ")
        if command[0] == "insert":
            # print(command)
            insert_position = int(command[1])
            insert_value = int(command[2])
            insert_in_list(my_list, insert_position, insert_value)
        elif command[0] == "print":
            print_list(my_list)
        elif command[0] == "remove":
            remove_value = command[1]
            # print(my_list,remove_value)
            my_list = remove_from_list(my_list, remove_value)
            # my_list = [x for x in my_list if (x != remove_value)]
            print("in remove " + str(my_list))
        elif command[0] == "append":
            append_value = int(command[1])
            append_in_list(my_list, append_value)
        elif command[0] == "pop":
            pop_from_list(my_list)
        elif command[0] == "reverse":
            reverse_list(my_list)
        elif command[0] == "sort":
            my_list.sort()
                
        
if __name__ == '__main__':
    main()