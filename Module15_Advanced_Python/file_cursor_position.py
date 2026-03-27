file = open("sample.txt", "r")

print(file.read(5))   # read first 5 characters

file.seek(0)

print(file.read())

file.close()