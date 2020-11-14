import os

# making a directory in the current directory
def makedir(dirName):
    os.mkdir(dirName)

dirName = input('Enter a directory name to make in current directory:')
makedir(dirName)
