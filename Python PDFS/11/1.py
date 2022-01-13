# 1. Write a program to read text file.


with open(file='sample_file.txt', mode='r') as f:  # context manager!
    print(f.read())
