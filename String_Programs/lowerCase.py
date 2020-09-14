#string functions
def lowerCase(sentence):
    lowerCaseLetters = []
    upperCaseLetters = []

    for letter in sentence:
        if letter.islower():
            lowerCaseLetters.append(letter)
        else:
            upperCaseLetters.append(letter)

    return ''.join(lowerCaseLetters + upperCaseLetters)


print(lowerCase("VHGIDUFhdighfgf"))
