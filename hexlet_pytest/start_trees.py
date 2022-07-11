def remove_first_level(tree):
    list1 = []
    lst2 = []
    for i in tree:
        if type(i) == list:
            list1.append(i)
    for it in list1:
        for item in it:
            lst2.append(item)
    return lst2
