def dictionary7():
    # dictionary traversal
    classroom1 = {
        "s1": {
            "name": "sam",
        },
        "s2": {
            "name": "ram",
        },
        "s3": {
            "name": "rahim",
        }
    }

    for x in classroom1.values():
        print(x)

    for x, y in classroom1.items():
        print(x, y)

    print(classroom1.get('s2'))
    print(classroom1['s3']['name'])



dictionary7()
