from bot.enums import Invalid


class InvalidMessageError(Exception):

    def __init__(self, type: Invalid, message: str):

        self.type: Invalid = type

        self.message: str = message

    def __str__(self):
        return self.message


class RepositoryError(Exception):

    def __init__(self, message: str):

        self.message: str = message

    def __str__(self):
        return self.message
