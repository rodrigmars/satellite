from enums import Invalid


class Occurrence:

    def __init__(self, id: int, author: str, total: int, type_occurrence: Invalid) -> None:
        self.id = id
        self.author = author
        self.total = total
        self.type_occurrence = type_occurrence
