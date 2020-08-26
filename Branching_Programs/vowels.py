def vowels(word):
    if (word[0] in 'AEIOU' or word[0] in 'aeiou'):
        if (word[len(word) - 1] in 'AEIOU' or word[len(word) - 1] in 'aeiou'):
            return 'First and last letter of ' + word + ' is vowel'
        else:
            return 'First letter of ' + word + ' is vowel'
    else:
        return 'Not a vowel'

print(vowels('ankara'))

