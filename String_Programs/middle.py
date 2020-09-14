#len
def getMiddle(strr):
    startIndex = int(len(strr) / 2 - 1)
    endIndex = startIndex + 3
    print(strr[startIndex:endIndex])
    return


print(getMiddle("Nonames"))
