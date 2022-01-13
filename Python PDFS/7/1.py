# A, B and C are classes. A is a super class. B is a sub class of A. C is a sub class of B.

# Create 2 methods in each class, 1st method is specific to each class and 2nd
# method (overridden method) should be in all three Classes A, B and C.

class A:
    def __init__(self, name: str):
        self.name = name
        print('class A ctor')

    def get_name(self):
        return 'A: ' + self.name


class B(A):
    def __init__(self, name: str):
        super().__init__(name)
        print('class B ctor')

    def get_name(self):
        return 'B: ' + self.name


class C(B):
    def __init__(self, name: str):
        super().__init__(name)
        print('class C ctor')

    def get_name(self):
        return 'C: ' + self.name


# Create a class with main method. Create an object for each class A, B and C in main
# method and call every method of each class using its own object/instance.

print()
a = A('a')
print(a.get_name())

print()
b = B('b')
print(b.get_name())

print()
c = C('c')
print(c.get_name())


# Call an overridden method with super class reference to B and C class’s objects.

print()
print(b.get_name())
print(c.get_name())


# Runtime Polymorphism with Data Members/Instance variables, Repeat the above process only for data members.

# ?
# Make a PR.
