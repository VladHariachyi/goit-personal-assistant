import re
from dataclasses import dataclass
from datetime import datetime
from ...shared.error_handler.decorators.catch_error import ValidationError


@dataclass
class Field:
    """The data field definition"""
    value: str

    def __str__(self) -> str:
        return str(self.value)
    
    
class Name(Field):
    """Contact name field."""

    def __init__(self, value: str):
        self.validate_required(value)
        super().__init__(value)

    def validate_required(self, value: str) -> None:
        if not value.strip():
            raise ValidationError("The name is required")


class Phone(Field):
    """Phone number field."""
    PHONE_PATTERN = r"^\+380\d{9}$"
    def __init__(self, value: str):
        value = value.strip()
        self.validate(value)
        super().__init__(value)

    @staticmethod
    def validate(value: str) -> None:
        """
        Validate Ukrainian phone format:
        +380XXXXXXXXX
        """

        if not re.fullmatch(
            Phone.PHONE_PATTERN,
            value
        ):
            raise ValidationError(
                "Phone number must be in format +380XXXXXXXXX"
            )


class Birthday(Field):
    """The birthday class definition, responsible for saving and validating the birthday date"""
    DATE_FORMAT: str = "%d.%m.%Y"

    def __init__(self, value):
        try:
            self.date = datetime.strptime(value, self.DATE_FORMAT)
        except ValueError:
            raise ValidationError("Invalid date format. Please use DD.MM.YYYY")