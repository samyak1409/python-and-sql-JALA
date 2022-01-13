# 3. Define a static variable and change within the instance.


class Class1:

    static_var = 'UNCHANGED'

    # def __init__(self): pass


instance = Class1()
print(instance.static_var)  # UNCHANGED

instance.static_var = 'changed'
print(instance.static_var)  # changed
print(Class1.static_var)  # UNCHANGED
