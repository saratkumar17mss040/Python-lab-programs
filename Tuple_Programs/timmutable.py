def immutableTuple():
    # tuples are immutable
    my_tuple = (1, 2, 3, 4, 5)
    try:
        my_tuple[0] = 10
    except TypeError:
        print('Tuples are immutable therefore tuple object does not support item assignment!!!')
    # however,tuples can be reassigned
    my_tuple = (6, 7)
    print(my_tuple)


immutableTuple()
