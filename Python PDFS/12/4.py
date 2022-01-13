# 4. Write a program which illustrates the concept of attributes of a constructor.


from i1 import Class1


# Attributes of Constructor:
print(Class1.__dict__)  # provide the dictionary containing the information about the class namespace.
print(Class1.__doc__)  # contain a string which has the class documentation.
print(Class1.__module__)  # access the module in which this class is defined.
print(Class1.__name__)  # access the class name.
