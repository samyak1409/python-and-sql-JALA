# 4. Write a program to print the odd and even numbers.


till = int(input('\nFrom 0 to?: '))

print('\nEven:')
for i in range(0, till+1, 2):
    print(i)

print('\nOdd:')
for i in range(1, till+1, 2):
    print(i)
