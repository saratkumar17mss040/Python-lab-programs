#string traversal
def getDictionary(sentence):
    countLetters = dict()
    for letter in sentence:
        count = sentence.count(letter)
        countLetters[letter] = count
    print(countLetters)


print(getDictionary('Swordsmanandthesea'))
