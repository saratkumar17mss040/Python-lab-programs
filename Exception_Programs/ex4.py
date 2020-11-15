def findFile():
    try:
        fileName = input('Enter a filename or path:')
        file = open(fileName)
        print(file.read())
    except FileNotFoundError:
        print('File not found error !')


findFile()
