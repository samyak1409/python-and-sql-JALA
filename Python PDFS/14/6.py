# 6. Write a program to create your own exception.


class CustomException(Exception):
    """This is a custom exception."""
    def __init__(self, message):
        self.message = message


try:
    raise CustomException('something went wrong')
except CustomException as e:
    print(e.message)
