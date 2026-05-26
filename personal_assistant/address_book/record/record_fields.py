from dataclasses import dataclass


@dataclass
class Field:
    value: str

    def __str__(self) -> str:
        return f"{self.value}"
    

class Name(Field):
    pass


class Phone(Field):
    pass