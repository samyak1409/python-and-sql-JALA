# 6. Write a program to check whether a file is having read access and write access permissions.


f = open(file='sample_file.txt', mode='r')
print(f.readable())  # True
print(f.writable())  # False (because file was opened in read mode)
