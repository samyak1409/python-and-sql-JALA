# 3. Define a static variable and change within the instance.


class Class:

    static_var = 'UNCHANGED'

    # def __init__(self): pass


instance = Class()
print(instance.static_var)  # UNCHANGED

instance.static_var = 'changed'
print(instance.static_var)  # changed
print(Class.static_var)  # UNCHANGED
