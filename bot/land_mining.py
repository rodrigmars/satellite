from utils import get_words, check_url
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


async def message_mining(message):

    domains = ["https://www.youtube.com/",
               "https://stackoverflow.com/",
               "https://stackoverflow.blog/",
               "https://github.com/",
               "https://www.geeksforgeeks.org/",
               "https://www.python.org/",
               "https://nodejs.org/en",
               "https://developer.mozilla.org/",
               "https://www.javascripttutorial.net/",
               "https://dev.java/",
               "https://dev.to/",
               "https://medium.com/"]

    async def valid_domain(url: str) -> bool:
        return False if url not in domains else True

    async def check_message() -> None:

        for word in await get_words(message):

            if await check_url(word):

                if not await valid_domain(word):

                    raise InvalidMessageError(Invalid.LINK,
                                              "Endereço de URL nao permitido")

    return check_message
