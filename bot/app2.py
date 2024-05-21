from land_mining import message_mining
from exceptions.custom_errors import InvalidMessageError


valid = message_mining("teste http://teste-atack")

try:
    valid()
except InvalidMessageError as exc:
    print(exc)
