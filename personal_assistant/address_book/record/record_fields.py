from dataclasses import dataclass
from datetime import datetime
from ...shared.error_handler.decorators.catch_error import ValidationError


@dataclass
class Field:
    """The data field definition"""
    value: str

    def __str__(self) -> str:
        return str(self.value)
    
    
@dataclass
class Name(Field):
    """Contact name field."""

    def __post_init__(self):
        self.validate_required(self.value)
        super().__post_init__()

    def validate_required(self, value: str):
        if not value.strip():
            raise ValueError("The name is required")


@dataclass
class Phone(Field):
    """Phone number field."""

    def __post_init__(self):
        self.value = self.value.strip()
        self.validate(self.value)

    @staticmethod
    def validate(value: str):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("The number must contain 10 digits")


class Birthday(Field):
    """The birthday class definition, responsible for saving and validating the birthday date"""
    def __init__(self, value):
        try:
            date = datetime.strptime(value, "%d.%m.%Y")
            self.date = date
        except ValueError:
            raise ValidationError("Invalid date format. Please use DD.MM.YYYY")

