def dictionary4():
    # using dict() method
    phone_no = dict({
        'sam': 1234567890,
        'ram': 9876543212,
    })
    students = dict([(1, 'sam'), (2, 'ram')])
    print(phone_no)
    print(students)
    # accessing dictionary values
    print(phone_no['sam'])
    print(phone_no.get('ram'))
    print(students.get(1))


dictionary4()
