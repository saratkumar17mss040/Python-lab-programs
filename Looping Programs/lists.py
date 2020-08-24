my_list = [1, 'sam', '3.14', 3.45, 'dinesh']
number_list = []
string_list = []
float_list = []

for i in my_list:
    if (str(i) == i):
        string_list.append(i)
    elif (int(i) == i):
        number_list.append(i)
    else:
        float_list.append(i)
    
print(string_list)
print(number_list)
print(float_list)
