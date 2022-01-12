# 10. Write a function to find the duplicate values of an array.


def duplicates(arr: list) -> list:
    from collections import Counter
    dic = Counter(arr)
    # print(dic)  # debugging
    return [i for i in dic.keys() if dic[i] > 1]


if __name__ == '__main__':  # because this file is being imported in files '11.py' and '12.py'
    print(duplicates(arr=[1, 2, 3, 2, 1]))  # [1, 2]


# this file has been renamed to i10 because it is being imported in files '11.py' and '12.py' and python doesn't allow number (i.e. 10) as an identifier
