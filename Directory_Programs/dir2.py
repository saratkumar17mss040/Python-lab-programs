import os

# getting directory path input from the user
# D:\Github_repos\Python-Lab-Programs\Directory_Programs
current_dir = input('Enter a directory path:')

if os.getcwd() == current_dir:
    print("Correct current path")
else:
    print("Not correct current path")
