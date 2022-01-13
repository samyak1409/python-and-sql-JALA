# 1. Write a class with a default constructor, one argument constructor and two argument constructors.
# Instantiate the class to call all the constructors of that class from a main class.


# Constructor overloading is not allowed in Python, but we can achieve the same behaviour by:


class Class1:
    """Demo Class 1"""

    def __init__(self, name: str = 'Default'):
        self.name = name
        print(name, 'Constructor')

    @classmethod  # (decorator)
    def from_single_arg(cls, arg: str):  # class method -> automatically takes class as an argument
        return cls(name=arg)

    @classmethod
    def from_double_arg(cls, arg1: str, arg2: str):
        return cls(name=arg1+' '+arg2)


if __name__ == '__main__':
    Class1()  # Default Constructor
    Class1.from_single_arg(arg='Argument')  # Argument Constructor
    Class1.from_double_arg(arg1='Double', arg2='Argument')  # Double Argument Constructor


# this file has been renamed to i1 because it is being imported in files '2.py' and python doesn't allow number (i.e. 1) as an identifier
