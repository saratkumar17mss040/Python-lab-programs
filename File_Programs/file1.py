f = open("sample.txt")
print("Reading relative file paths")
print(f.read())
print("Reading files from absolute paths")
f = open("D:/DOC FILES/COLLEGE DOCUMENTS/6TH SEMESTER FILES AND PPT/PYTHON/sample2.txt")
print(f.read())
f = open("sample.txt", mode="r", encoding="utf-8")
print("Reading first 5 characters")
print(f.read(5))
