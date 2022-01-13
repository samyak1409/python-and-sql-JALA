# 7. Write a program with finally block.


try:
    print('trying')
    print(21/0)
except ZeroDivisionError:
    print('can\'t divide by zero')
finally:
    print('exiting')
