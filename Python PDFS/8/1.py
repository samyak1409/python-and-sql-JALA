# 1. Create a class with PRIVATE fields, private method and a main method.
# Print the fields in main method.
# Call the private method in main method.

class Class:

    __priv_class_var = 'am a private field'

    @staticmethod  # so that don't take self as an argument
    def __priv_method():
        print('private method called')

    def main(self):
        print(self.__priv_class_var)
        self.__priv_method()
        print()  # (spacing)


ob = Class()
ob.main()


# Create a sub class and try to access the private fields and methods from sub class.

class SubClass(Class):

    def method(self):

        print('> accessing public method "main"')
        self.main()  # public method accessible ✔

        print('> accessing private field "__priv_class_var"')
        try:
            print(self.__priv_class_var)
        except Exception as e:
            print('ERROR:', e)

        print()  # (spacing)

        print('> accessing private method "__priv_method"')
        try:
            self.__priv_method()
        except Exception as e:
            print('ERROR:', e)


ob2 = SubClass()
ob2.method()
