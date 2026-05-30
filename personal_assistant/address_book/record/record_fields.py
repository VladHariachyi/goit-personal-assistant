import re
from datetime import datetime

from ...shared.models import Field
from ...shared.error_handler import AddressBookError 

    
class Name(Field):
    """Contact name field."""

    def __init__(self, value: str):
        self.validate_name(value)
        super().__init__(value)

    def validate_name(self, value: str) -> None:
        if not value:
            raise AddressBookError("Please enter a name.")
        if not re.search(r"[A-Za-zА-Яа-яЁёІіЇїЄє]", value):
            raise AddressBookError("Name should contain at least one letter (for example, John or Anna).")


class Phone(Field):
    """Phone number field."""
    PHONE_PATTERN = r"^\+380\d{9}$"
    
    def __init__(self, value: str):
        value = value.strip()
        Phone.validate(value)
        super().__init__(value)

    @staticmethod
    def validate(value: str) -> None:
        """
        Validate Ukrainian phone format:
        +380XXXXXXXXX
        """

        if not re.fullmatch(Phone.PHONE_PATTERN,value):
            raise AddressBookError("Invalid phone number format. Use: +380991234567")


class Birthday(Field):
    """The birthday class definition, responsible for saving and validating the birthday date"""
    DATE_FORMAT: str = "%d.%m.%Y"

    def __init__(self, value: str):
        try:
            self.date = datetime.strptime(value, self.DATE_FORMAT)
        except ValueError:
            raise AddressBookError("Invalid date format. Use: 25.12.1995")
        super().__init__(value)


class Email(Field):
    """Email field."""
    EMAIL_REGEX = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

    def __init__(self, value: str):
        value = value.strip()
        self.validate(value)
        super().__init__(value)

    def validate(self, value: str) -> None:
        if not self.EMAIL_REGEX.match(value):
            raise AddressBookError("Invalid email format. Use: name@example.com")
        

class Address(Field):
    """Address field."""

    def __init__(self, value: str):
        value = value.strip()
        self.validate(value)
        super().__init__(value)

    def validate(self, value: str) -> None:
        if not re.search(r"[A-Za-zА-Яа-я]", value):
            raise AddressBookError("Address must contain letters (for example, Baker Street 221B).")