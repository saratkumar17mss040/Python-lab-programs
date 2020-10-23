def dictionary9():
    employee_dict = {
        'name': 'sam',
        'company': 'abc',
        'role': 'software architect',
    }
    # using len()
    print(len(employee_dict))
    # using keys()
    keyCounter = 0
    for key, value in employee_dict.items():
        print(key + ':', value)
        keyCounter = keyCounter + 1
    return keyCounter


print(dictionary9())
