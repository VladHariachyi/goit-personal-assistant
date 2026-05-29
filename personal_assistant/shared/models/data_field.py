from dataclasses import dataclass


@dataclass
class Field:
    """The data field definition"""
    value: str

    def __str__(self) -> str:
        return str(self.value)