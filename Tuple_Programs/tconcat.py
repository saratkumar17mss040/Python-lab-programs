def tconcat(my_tuple):
    # tuple concatenation
    another_tuple = (5, 6, 7, 8, 9, 10)
    # using + operator
    final_tuple = my_tuple + another_tuple
    print(final_tuple)
    # using sum method
    sum_tuple = sum((my_tuple, another_tuple), ())
    print(sum_tuple)


tconcat((1, 2, 3, 4, 5))
