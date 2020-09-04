def counter(strr):
    lowerCaseCounter = 0
    upperCaseCounter = 0
    numberCounter = 0
    specialCounter = 0

    for letter in strr:
        if letter.islower():
            lowerCaseCounter = lowerCaseCounter + 1
        elif letter.isupper():
            upperCaseCounter = upperCaseCounter + 1
        elif letter.isnumeric():
            numberCounter = numberCounter + 1
        else:
            specialCounter = specialCounter + 1

    print("Number of lowercase characters:" + str(lowerCaseCounter))
    print("Number of uppercase characters:"+str(upperCaseCounter))
    print("Number of number characters:"+str(numberCounter))
    print("Number of special characters:" + str(specialCounter))

    return


counter("sjdchiudfhdsofiuf5796843v54q2!##$")
