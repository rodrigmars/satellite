import re


def check_url(text):
    return True if re.match(
        r"(https?|ftp)://"
        r"(\w+(\-\w+)*\.)?"
        r"((\w+(\-\w+)*)\.(\w+))"
        r"(\.\w+)*"
        r"([\w\-\._\~/]*)*(?<!\.)", text) else False


def get_words(text):
    return re.sub(
        '[,@_!#$%^&*()<>?\\|\\[\\]}{~]', ' ', text).split()
