import os, shutil

def removeEmptyDir(dirName):
    os.rmdir(dirName)

def removeNonEmptyDir(dirName):
    shutil.rmtree(dirName)

# current working directory
emptyDirectoryName = input('Enter an empty directory name to remove:')
nonEmptyDirectoryName = input('Enter an non empty directory name to remove:')

removeEmptyDir(emptyDirectoryName)
removeNonEmptyDir(nonEmptyDirectoryName)

