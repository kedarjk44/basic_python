if __name__ == '__main__':
    no_of_students = int(input())
    assert(no_of_students >= 2)
    assert(no_of_students <= 5)
    #print(no_of_students)
    stud_dict = {}
    for i in range(no_of_students):
        stud_name = str(input())
        stud_score = float(input())
        stud_dict[stud_name] = stud_score
    #print(stud_dict)
    keylist = list(stud_dict.keys())    
    values = list(stud_dict.values())
    #print(values)
    unique_values = set(values)
    unique_values = list(unique_values)
    unique_values.sort()
    #print(values[1], values[2])
    out_list = []    
    for key in keylist:
        if stud_dict[key] == unique_values[1]:
            out_list.append(key)
    out_list.sort()
    for member in out_list:
        print(member)