#concatenation
def concatenation(str1, str2):
    str3 = str1 + ' ' + str2
    print(str3)
    str4 = " ".join([str1, str2])
    print(str4)
    print("% s % s" % (str1, str2))
    print("{} {}".format(str1, str2))


print(concatenation("The man who knew","infinity"))