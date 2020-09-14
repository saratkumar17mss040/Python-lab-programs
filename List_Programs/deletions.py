# pop(), del, remove, clear()
def deletions(my_list):
    #my_list without any operations on it
    print(my_list)
    # deleting last element using pop()
    my_list.pop()
    print(my_list)
    # deleting element based on index
    my_list.pop(1)
    print(my_list)
    # using del keyword to delete based on index
    del my_list[2]
    print(my_list)
    # using remove() method to delete an element
    my_list.remove('4')
    print(my_list)
    # using clear() method to empty the list
    my_list.clear()
    print(my_list)
    # using del keyword to delete the entire list
    del my_list
    # print(my_list)


deletions([9,'2','4','5','40'])
