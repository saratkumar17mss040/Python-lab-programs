def tmembership(my_tuple1,my_tuple2):
    for item in my_tuple1:
        # membership in and not in operator in tuple
        if item in my_tuple2:
            print(str(item) + ' in my_tuple2')
        if item not in my_tuple2:
            print(str(item) + ' not in my_tuple2')


print(tmembership((1, 2, 3, 4, 5), (1, 2, 3)))
