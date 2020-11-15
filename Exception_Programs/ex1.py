def ex1(num1, num2):
    try:
        res = num1 / num2
    except ZeroDivisionError:
        print('division by zero error')


ex1(1,0)