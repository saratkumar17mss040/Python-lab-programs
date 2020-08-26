def checkNumber(num):
    if num > 50:
        if num % 2 == 0:
            return 'The given number ' + str(num) + ' is greater than 50 and divisible by 2'
        else:
            return 'The given number ' + str(num) + ' is greater than 50 but not divisible by 2'
    else:
        return 'The given number ' + str(num) + ' is lesser than 50'


print(checkNumber(60))
print(checkNumber(24))
print(checkNumber(55))
