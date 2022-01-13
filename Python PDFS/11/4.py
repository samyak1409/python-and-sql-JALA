# 4. Write a program to read a file stream supports random access.


f = open(file='sample_file.txt')

print(f.seekable())  # seekable() Returns True if the file stream supports random access
# which means that we can read the file from anywhere using seek()
# https://www.programiz.com/python-programming/file-operation#:~:text=seekable(),supports%20random%20access.

f.seek(29)  # move the cursor to that position
print('"')
print(f.read())
print('"')
