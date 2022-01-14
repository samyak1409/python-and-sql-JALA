# 2. Define a static variable and access that through a instance.


class Class:

    static_var = '21'

    # def __init__(self): pass


instance = Class()
print(instance.static_var)  # 21
