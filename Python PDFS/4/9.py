# 9. Write a function to reverse an array of integer values.


def reverse(arr: list) -> None:
    n = len(arr)
    for i in range(n//2):  # iterate half times
        arr[i], arr[n-1-i] = arr[n-1-i], arr[i]  # swap


a = [1, 2, 3, 4]
reverse(a)
print(a)  # [4, 3, 2, 1]
