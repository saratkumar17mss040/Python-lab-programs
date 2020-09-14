# general list
def add():
    my_list = [2, 4, 8]
    print('Enter the number of elements to enter into the list:')
    numberOfElements = int(input())
    i = 0
    while(i < numberOfElements):
        element = input()
        my_list.append(element)
        i = i + 1
    return my_list


print(add())
