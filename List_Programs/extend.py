# extend method 
def extend(my_list):
    colors_list = ['red','blue','green','yellow']
    my_list.extend(colors_list)
    return my_list

print(extend([1,2,3,4,5]))