# 5. Write a program to read a file a just to a particular index using seek().


with open(file='sample_file.txt', mode='r') as f:
    f.seek(29)
    print(f.read())
