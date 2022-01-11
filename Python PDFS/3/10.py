# 10. Write a program to palindrome or not.


string = input('Str: ')
n = len(string)//2
# print(n)  # debugging
# print(string[:n], string[:-n-1:-1])  # debugging
print('Palindrome' if string[:n] == string[:-n-1:-1] else 'Not Palindrome')
