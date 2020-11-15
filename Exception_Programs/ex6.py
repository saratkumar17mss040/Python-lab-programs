def variousException():
    my_list = [1, 2, 3, 4]
    try:
        a = 5
        print(a)
        print(my_list[5])
    except (NameError, IndexError):
           print('Error')

variousException()