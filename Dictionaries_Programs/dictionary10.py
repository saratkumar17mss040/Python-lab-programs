def dictionary10():
    numbers = {1: 44, 2: -12, 4: 13, 3: 4, 6: -5, 5: 76}
    print(numbers)
    # sorted keys
    print(sorted(numbers.keys()))
    # sorted keys with values
    print(sorted(numbers.items()))
    # sort by values
    print(sorted(numbers.values()))
    # reverse sort values - desc to asce
    print(sorted(numbers.values(), reverse=True))
    # reverse sort keys
    print(sorted(numbers.keys(), reverse=True))
    # reverse sort values
    print(sorted(numbers.values(), reverse=True))
    # back to dictionary - sorted only based on keys on key pair values
    print(dict(sorted(numbers.items(), reverse=True)))


dictionary10()
