import re
word = input('Enter a word:')
vowels = ('a', 'e', 'i', 'o', 'u')
for letter in word.lower():
    if letter in vowels:
        word = word.replace(letter, "")

print(word)
