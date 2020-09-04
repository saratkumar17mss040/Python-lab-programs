def asterisk(sentence):
    subStrings = sentence.split('*')
    for s in subStrings:
        print(s)

print(asterisk('hello*world*i*am*sarath'))