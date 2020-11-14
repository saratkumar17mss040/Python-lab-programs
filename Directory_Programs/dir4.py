import os

# making a directory in the specified path 
# D:\Github_repos\Python-Lab-Programs\rootDirectory
def makedir(dirName):
    os.mkdir(dirName)


dirName = input('Enter a directory name to make in the specifed path :')
makedir(dirName)
