# 2. Call the constructors (both default and argument constructors) of super class from a child class.


from i1 import Class1


class Class2(Class1):
    pass


Class2()  # Default Constructor
Class2.from_single_arg(arg='Second')  # Second Constructor
