# 3. Create a class with PUBLIC fields and methods.

class AClass:

    public_class_var = 'am a public field'

    @staticmethod  # so that don't take self as an argument
    def public_method():
        print('public method called')


# Access the public methods and fields from any class in the same package or different package.

class AnyClass:

    @staticmethod  # so that don't take self as an argument
    def method():
        print(AClass.public_class_var)
        AClass.public_method()


AnyClass.method()


# not sure if this is what the questioner wanted.
# Make a PR.
