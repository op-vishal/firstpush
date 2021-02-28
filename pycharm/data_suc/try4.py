def sub_lists(l):
    base = []
    lists = [base]
    for i in range(len(l)):
        orig = lists[:]
        print(orig)
        new = l[i]
        for j in range(len(lists)):
            lists[j] = lists[j] + [new]
        lists = orig + lists

    return lists


# driver code
l1 = [1, 2, 3]
print(sub_lists(l1))