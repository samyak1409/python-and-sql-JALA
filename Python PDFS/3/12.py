# 12. Print gender (Male/Female) program according to given M/F using switch.


gender = input('Gender (m/f): ').casefold()

match gender:
    case 'm':
        print('Male')
    case 'f':
        print('Female')
    case _:
        print('Please try again.')
