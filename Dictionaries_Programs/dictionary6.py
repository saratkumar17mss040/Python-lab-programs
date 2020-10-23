def dictionary6():
    # using dict() method
    phone_no = dict({
        'sam': 1234567890,
        'ram': 9876543212,
    })
    clear_dictionary = {
        'name': 'bane'
    }
    print(clear_dictionary)
    students = dict([(1, 'sam'), (2, 'ram')])
    print(phone_no)
    print(students)
    # removing dictionary key value
    print(phone_no.pop("sam"))
    print(phone_no)
    # removing last item
    print(students.popitem())
    print(students)
    # del
    del phone_no['ram']
    print(phone_no)
    # using clear()
    clear_dictionary.clear()
    print(clear_dictionary)



dictionary6()
