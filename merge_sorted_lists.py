def merge_sorted_lists(lst1, lst2):
    op_lst = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            op_lst.append(lst1[i])
            i += 1
        else:
            op_lst.append(lst2[j])
            j += 1
    op_lst += lst1[i:len(lst1)]
    op_lst += lst2[j:len(lst2)]
    return op_lst


lst1 = [1, 5, 7, 8, 13]
lst2 = [2, 3, 4, 6, 9, 11, 12]
print(merge_sorted_lists(lst1, lst2))
