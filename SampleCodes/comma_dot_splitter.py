import re


def splitter(num_inp):
    comma_split_list = re.split(",", num_inp)
    out_list = []
    for item in comma_split_list:
        #print(item, bool(re.search("\.",item)))
        dot_split_list = []
        if (bool(re.search("\.",item))):
            #print("Here")
            dot_split_list.append(re.split("\.",item))
            #print(dot_split_list)
            for dot_item in dot_split_list:
                out_list.append(dot_item)
        else:
            if(item != ""):
                out_list.append(item)
    print(out_list)
    for member in out_list:
        if (isinstance(member,list)):
            for mem in member:
                if (mem != ""):
                    print(mem)
        else:
            print(member)


def main():
    num_inp = ",1,2,3,4.04,"
    splitter(num_inp)


if __name__ == "__main__":
    main()