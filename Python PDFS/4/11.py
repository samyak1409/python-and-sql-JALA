# 11. Write a program to find the common values between two arrays.


def commons(arr1: list, arr2: list) -> list:  # TC= O(n); SC= O(n)
    from i10 import duplicates
    return duplicates(arr=list(set(arr1))+list(set(arr2)))


print(commons(arr1=[1, 2, 3], arr2=[1, 2, 3, 4, 5]))  # [1, 2, 3]
