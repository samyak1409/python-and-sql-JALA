# 2. Write a program to write text to .txt file using InputStream.


some_text = input('Write anything: ')
with open(file='sample_file.txt', mode='a') as f:
    f.write(some_text)
