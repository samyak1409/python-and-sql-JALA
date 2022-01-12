# 8. Write a function to find the minimum and maximum value of an array.


def min_n_max(arr: list) -> tuple:
    min_, max_ = float('inf'), float('-inf')
    for i in arr:
        if i < min_:
            min_ = i
        elif i > max_:
            max_ = i
    return min_, max_


if __name__ == '__main__':  # because this file is being imported in file '16.py'
    print(min_n_max(arr=[1, 2, 3]))  # (1, 3)

# this file has been renamed to i10 because it is being imported in file '16.py' and python doesn't allow number (i.e. 8) as an identifier
