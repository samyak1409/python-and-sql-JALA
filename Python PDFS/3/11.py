# 11. Program to check whether a number is EVEN or ODD using switch.


n = int(input('n: '))

match n % 2:  # 👌
    case 0:
        print('even')
    case 1:
        print('odd')
