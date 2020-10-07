# itertools library
from itertools import repeat


def trepeat():
    my_tuple = ('it\'s', 'something', 'confusing')
    # repeat using * operator
    print(my_tuple * 3)
    # repeat using repeat method
    print(tuple(repeat(my_tuple, 5)))


trepeat()
