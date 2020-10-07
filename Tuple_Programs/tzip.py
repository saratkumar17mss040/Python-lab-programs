def tzip():
    string_list = ['man', 'cub', 'desk']
    num_tuple = (1, 2, 3)
    mixed_tuple = (1, True, 3.14)
    # zip function
    res = zip(string_list, num_tuple, mixed_tuple)
    # converting to set object
    print(set(res))


print(tzip())
