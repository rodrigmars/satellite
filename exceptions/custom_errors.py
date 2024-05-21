from enum import Enum


class Invalid(Enum):
    WORD = 1
    LINK = 2


class InvalidMessageError(Exception):

    def __init__(self, type: Invalid, message: str):

        self.type: Invalid = type

        self.message: str = message

    def __str__(self):
        return self.message
