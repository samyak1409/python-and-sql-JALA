# 3. Apply private, public, protected and default access modifiers to the constructor.


# A Class in Python has three types of access modifiers:
# Public Access Modifier (default)
# Protected Access Modifier (by adding '_')
# Private Access Modifier (by adding '__')

class Class3:

    def __init__(self, public, _protected, __private):
        self.public = public
        self._protected = _protected
        self.__private = __private


instance = Class3(1, 2, 3)

print(instance.public)  # -> easily be accessed
print(instance._protected)  # -> gives warning (Access to a protected member _protected of a class)
print(instance.__private)  # -> gives error (AttributeError: 'Class3' object has no attribute '__private')
