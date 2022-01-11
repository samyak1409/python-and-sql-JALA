# 8. Write a program to find Armstrong number or not.


# Armstrong number is a number that is equal to the sum of cubes of its digits.
# Hence 153 because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.

n = input('n: ')

n_ = 0
for digit in n:
    n_ += int(digit) ** 3
# print(n_)  # debugging

print('Armstrong' if int(n) == n_ else 'Not Armstrong')
