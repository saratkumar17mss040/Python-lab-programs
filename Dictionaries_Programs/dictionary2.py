def dictionary2():
    # general dictionary 2
    phone_no = {
        'sam': 1234567890,
        'ram': 9876543212,
    }
    # using copy()
    phone_no2 = phone_no.copy()
    print(phone_no2)
    print(phone_no)
    return phone_no2 == phone_no2


print(dictionary2())
