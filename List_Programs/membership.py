def membership(list1, list2):
    for item in list1:
        # membership in and not in operator 
        if item in list2:
            print(str(item) + ' in list2')
        if item not in list2:
            print(str(item) + ' not in list2')


print(membership([1,2,3,4,5],[1,2,3,6]))


