# 1. Create an abstract class with abstract and non-abstract methods.

from abc import ABC, abstractmethod  # -> using these both the stuffs is compulsory, otherwise class and method will not be ABSTRACT


class AbstractClass(ABC):  # # https://www.geeksforgeeks.org/abstract-classes-in-python/

    @abstractmethod
    def abstract_method(self):
        pass

    @staticmethod  # so that don't take self as an argument
    def non_abstract_method():
        print('non-abstract method called')


# instance = AbstractClass()  # -> TypeError: Can't instantiate abstract class AbstractClass with abstract method abstract_method


# 2. Create a sub class for an abstract class.
# Create an object in the sub class for the abstract class and access the non-abstract methods.

class SubClass(AbstractClass):

    def abstract_method(self):  # sub class must implement all abstract methods!
        print('abstract method IMPLEMENTED in the sub class (by overriding) and called')


instance = SubClass()
instance.non_abstract_method()
print()  # (spacing)


# 3. Create an instance for the child class in child class and call abstract methods.

instance.abstract_method()
print()  # (spacing)


# 4. Create an instance for the child class in child class and call non-abstract methods.

instance.non_abstract_method()
