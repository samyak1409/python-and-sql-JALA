# 9. Write a program to find the prime or not.


n = int(input('n: '))

if n > 1:

    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            print('not prime')
            break  # divided by some number
    else:
        print('prime')

else:
    print('not prime')
