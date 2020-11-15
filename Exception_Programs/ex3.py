def chicken():
    egg()


def egg():
    chicken()


try:
    chicken()
    egg()
except RecursionError:
    print("Recursion error !")
