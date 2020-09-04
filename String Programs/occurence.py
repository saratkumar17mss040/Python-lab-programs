def occurence(sentence,findWord):
    lowerString = sentence.lower()
    findWord = findWord.lower()
    return lowerString.count(findWord)


print(occurence("pink green red bule green","green"))
            