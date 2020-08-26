def even_num(list):
    my_list = []
    for n in list:
        if n % 2 == 0:
            my_list.append(n)
    return my_list


print(even_num([11, 21, 32, 41, 25, 7, 17, 8, 9]))
