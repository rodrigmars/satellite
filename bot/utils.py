import re


async def check_url(text) -> bool:
    return True if re.match(
        r"(https?|ftp)://"
        r"(\w+(\-\w+)*\.)?"
        r"((\w+(\-\w+)*)\.(\w+))"
        r"(\.\w+)*"
        r"([\w\-\._\~/]*)*(?<!\.)", text) else False


async def get_words(text) -> list[str]:
    return re.sub(
        '[,@_!#$%^&*()<>?\\|\\[\\]}{~]', ' ', text).split()
