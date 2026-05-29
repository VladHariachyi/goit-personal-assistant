from dataclasses import dataclass
from datetime import datetime
import re
from ...shared import AddressBookError


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
            raise AddressBookError("The name is required")


class Phone(Field):
    """Phone number field."""

    def __init__(self, value: str):
        value = value.strip()
        self.validate(value)
        super().__init__(value)

    def validate(self, value: str) -> None:
        """Validate phone number format (10 digits)."""
        if len(value) != 10 or not value.isdigit():
            raise AddressBookError("The number must contain 10 digits")


class Birthday(Field):
    """The birthday class definition, responsible for saving and validating the birthday date"""
    DATE_FORMAT: str = "%d.%m.%Y"

    def __init__(self, value):
        try:
            self.date = datetime.strptime(value, self.DATE_FORMAT)
            print('try birthday class', self.date)
        except ValueError:
            raise AddressBookError("Invalid date format. Please use DD.MM.YYYY")


class Email(Field):
    """Email field."""

    def __init__(self, value: str):
        value = value.strip()
        self.validate(value)
        super().__init__(value)

    def validate(self, value: str) -> None:
        EMAIL_REGEX = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
        if not EMAIL_REGEX.match(value):
            raise AddressBookError("Invalid email format")
        

class Address(Field):
    """Address field."""

    def __init__(self, value: str):
        value = value.strip()
        self.validate(value)
        super().__init__(value)

    def validate(self, value: str) -> None:
        if not re.search(r"[A-Za-zА-Яа-я]", value):
            raise AddressBookError("Address must contain letters")