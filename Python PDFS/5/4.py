# 4. Define a static variable and change within the class.


class Class:

    static_var = 'UNCHANGED'

    # def __init__(self): pass


print(Class.static_var)  # UNCHANGED

Class.static_var = 'changed'
print(Class.static_var)  # changed
instance = Class()
print(instance.static_var)  # changed
