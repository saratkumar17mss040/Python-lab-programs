def fact(num):

    if num == 1:
        return 1
    else:
        return (num * fact(num-1))

num = 4
print("factorial = ", fact(num))
