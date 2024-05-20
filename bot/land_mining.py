from utils import get_all_links, get_domain
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


def message_mining(message):

    allowed_domains = ["www.youtube.com",
                       "youtube.com",
                       "stackoverflow.com",
                       "stackoverflow.blog",
                       "github.com",
                       "www.geeksforgeeks.org",
                       "www.python.org",
                       "nodejs.org",
                       "developer.mozilla.org",
                       "www.javascripttutorial.net",
                       "dev.java",
                       "dev.to",
                       "medium.com"]

    def check_message() -> None:

        def compar_urls(domain: str) -> bool:
            return True if domain in allowed_domains else False

        for web_link in get_all_links(message):

            if not compar_urls(get_domain(web_link)):
                raise InvalidMessageError(Invalid.LINK,
                                          f"Web link '{web_link}' nao permitido!")

    return check_message
