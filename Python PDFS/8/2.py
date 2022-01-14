# 2. Create a class with PROTECTED fields and methods.

class AClass:

    _protected_class_var = 'am a protected field'

    @staticmethod  # so that don't take self as an argument
    def _protected_method():
        print('protected method called')


# Access these fields and methods from any class in the same package.

class AnyClass:

    @staticmethod  # so that don't take self as an argument
    def method():
        print(AClass._protected_class_var)  # -> gives warning (Access to a protected member _protected_class_var of a class)
        AClass._protected_method()  # -> gives warning (Access to a protected member _protected_method of a class)


AnyClass.method()


# Also, Access the PROTECTED fields and methods from child class located in a different package.
# Access the PROTECTED fields and methods from any class in different package.

# Make a PR.
