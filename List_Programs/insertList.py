# insert and append
def insertList(my_list):
    my_list.insert(0,'1')
    my_list.insert(1, '2')
    my_list.append(7)
    my_list[3:3] = [9, 2, 4]
    return my_list

print(insertList(['Wrath','Of','War',1,2,3]))