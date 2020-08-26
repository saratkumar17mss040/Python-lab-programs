def reverse(arg):
    if type(arg) == bool:
        return not (arg)
    else:
        return 'boolean expected'

print(reverse(True))