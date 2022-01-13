# 4. Write a program with multiple catch blocks.


try:
    denominator = int(input('Enter a num: '))
    print(21/denominator)
except ValueError:
    print('enter a valid num')
except ZeroDivisionError:
    print('can\'t divide by zero')
