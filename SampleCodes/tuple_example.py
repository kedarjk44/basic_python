def main():
    # no_of_spaces = int(input())
    # inp = input()
    # my_tup_list = inp.split(" ")
    # my_int_tup_list = []
    # for i in range(len(my_tup_list)):
    #     my_int_tup_list.append(int(my_tup_list[i]))
    # #print(my_int_tup_list)
    # tup = tuple(my_int_tup_list)
    # print(hash(tup))
    tup = (1, 2, 3, 4, 5)
    for i in range(len(tup)):
        print(tup[i])
    print(*tup)
    # tup[2] = 7


if __name__ == '__main__':
    main()
