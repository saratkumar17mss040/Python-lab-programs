import os

# rename current working directory


def changeDir(oldDirName, newDirName):
    os.rename(oldDirName, newDirName)


oldDirName = input('Enter the old directory name:')
newDirName = input('Enter the new directory name to rename the old one:')


changeDir(oldDirName, newDirName)
