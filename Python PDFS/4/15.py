# 15. Write a method to find number of even number and odd numbers in an array.


def even_odd_count(arr: list) -> tuple:
    e = o = 0
    for i in arr:
        if i % 2 == 0:
            e += 1
        else:
            o += 1
    return e, o


print('e, o:', even_odd_count(arr=[0, 1, 1, 2, 3]))  # e, o: (2, 3)
