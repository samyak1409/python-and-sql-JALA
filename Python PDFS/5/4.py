# 4. Define a static variable and change within the class.


class Class1:

    static_var = 'UNCHANGED'

    # def __init__(self): pass


print(Class1.static_var)  # UNCHANGED

Class1.static_var = 'changed'
print(Class1.static_var)  # changed
instance = Class1()
print(instance.static_var)  # changed
