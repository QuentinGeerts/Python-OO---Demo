class CustomError(Exception):

    def __init__(self, message):
        self.__message = message

    @property
    def message(self):
        return self.__message
    

if __name__ == '__main__':
    raise CustomError("Hello")
