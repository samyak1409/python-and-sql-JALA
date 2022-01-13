# 3. Write a program to read a file stream.


with open(file='sample_file.txt', mode='r') as f:  # streaming using next
    for _ in range(int(input('Read how many lines?: '))):
        try:
            print(next(f), end='')
        except StopIteration:
            print('<Reached at the end of the file.>')
            break
