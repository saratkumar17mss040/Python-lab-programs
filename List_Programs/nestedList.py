# list traversing
def printList(simpleList, nestedList):
    for item in simpleList:
        print(item)

    for item in nestedList:
        print(item)
    return


printList([1, 'data', True], [1, 2, 3, [False,True], 'nil'])

