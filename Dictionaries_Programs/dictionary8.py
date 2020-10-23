def dictionary8():
    # membership operator in / not in 
    student1 = {
        'name': 'sam',
        'rollno': 2,
        'mark1': 45,
        'mark2': 50,
        'mark3': 70,
    }
    student2 = {
        'name': 'ram',
        'rollno': 3,
        'mark3': 55,
    }
    print(student1)
    print(student2)
    for key in student1:
        if key in student2:
            print(key + ' is present')
        elif key not in student2:
            print(key + ' is not present')


dictionary8()
