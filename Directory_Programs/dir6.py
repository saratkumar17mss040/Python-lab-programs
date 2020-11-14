import os

# rename directory based on given path by the user


def changeDir(oldDirName, newDirName):
    os.rename(oldDirName, newDirName)


# D:\Github_repos\Python-Lab-Programs\rootDirectory
oldDirName = input('Enter the old directory name with path:')
# D:\Github_repos\Python-Lab-Programs\headDirectory
newDirName = input(
    'Enter the new directory name to rename the old one with path:')

changeDir(oldDirName, newDirName)
