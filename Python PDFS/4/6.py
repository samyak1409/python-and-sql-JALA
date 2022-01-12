# 6. Write a function to copy an array to another array.


def copy_arr(from_: list, to: list) -> None:
    t, f = len(to), len(from_)
    for i in range(0, min(t, f)):
        to[i] = from_[i]  # directly updating
    if t < f:  # more elements to paste
        for i in range(t, f):
            to.append(from_[i])
    elif t > f:  # copying done, deleting additional values
        for _ in range(t-f):
            to.pop()


a1, a2 = [1, 2], [3]
copy_arr(from_=a1, to=a2)
print(a1, a2)  # [1, 2] [1, 2]

a1, a2 = [1, 2], [3, 2, 1]
copy_arr(from_=a1, to=a2)
print(a1, a2)  # [1, 2] [1, 2]
