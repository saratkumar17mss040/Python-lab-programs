import os

fileName = input("Enter file name to rename it:")
os.rename('sample3.txt', fileName)
print("filename successfully renamed")
