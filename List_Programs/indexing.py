def indexing(my_list):
    firstItem = my_list[0]
    lastItem = my_list[len(my_list) - 1]
    negativeIndexing = my_list[-2]
    # normal copy
    my_list_copy = my_list
    print(my_list_copy)
    # using copy method
    my_list_copy2 = my_list.copy()
    print(my_list_copy2)
    slicing = my_list[0:4]
    return [firstItem,lastItem,negativeIndexing,slicing]

print(indexing([1,2,3,4,5]))
