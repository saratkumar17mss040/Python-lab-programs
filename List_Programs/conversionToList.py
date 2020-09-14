def conversion(my_tuple):
    my_list = list(my_tuple)
    # list slicing
    my_sliced_list = my_list[2:]
    print(my_sliced_list)
    return my_list

print(conversion(('well', 'bad', 'bitter', 'truth')))
