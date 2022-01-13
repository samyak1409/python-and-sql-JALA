# 3. Write a method which throws exception, Call that method in main class without try block.


def func():
    raise Exception('Custom')


func()  # Exception: Custom
