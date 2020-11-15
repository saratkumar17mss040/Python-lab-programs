def errorWithFinally():
    try:
        print(b)
    except NameError:
        print('Name error as b is not declared !')
    finally:
        # good use case for finally would be closing files, closing  network connection
        print('No matter what i will be executed at the end of the programs')


errorWithFinally()