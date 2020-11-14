import os
import shutil


def removeEmptyDir(dirName):
    os.rmdir(dirName)


def removeNonEmptyDir(dirName):
    shutil.rmtree(dirName)


# absolute path directory

# D:\Github_repos\Python-Lab-Programs\Directory_Programs\salim
emptyDirectoryName = input('Enter an empty directory name to remove:')
# D:\Github_repos\Python-Lab-Programs\Directory_Programs\aj
nonEmptyDirectoryName = input('Enter an non empty directory name to remove:')

removeEmptyDir(emptyDirectoryName)
removeNonEmptyDir(nonEmptyDirectoryName)
