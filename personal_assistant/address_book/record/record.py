from .record_fields import Name, Phone, Birthday, Email, Address
from ...shared import AddressBookError


class Record():
    """Stores contact name and list of phones."""

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.emails = []
        self.birthday = None
        self.address = None

    def change_contact_name(self, name: str) -> None:
        pass

    def add_phone(self, value: str) -> None:
        if any(phone.value == value for phone in self.phones):
            raise AddressBookError("This number already exists")
        self.phones.append(Phone(value))

    def remove_phone(self, value: str) -> None:
        phone = self.find_phone(value)
        self.phones.remove(phone)

    def edit_phone(self, old_number: str, new_number: str) -> None:
        if old_number == new_number:
            raise AddressBookError("New phone must be different from old phone")
        old_phone = self.find_phone(old_number)
        new_phone = Phone(new_number)
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone

    def find_phone(self, value: str) -> None:
        for phone in self.phones:
            if phone.value == value:
                return phone
        raise AddressBookError("Phone not found")
    
    def add_email(self, value: str) -> None:
        if any(email.value == value for email in self.emails):
            raise AddressBookError("This email already exists")
        self.emails.append(Email(value))

    def remove_email(self, value: str) -> None:
        email = self.find_email(value)
        self.emails.remove(email)

    def find_email(self, value: str) -> None:
        for email in self.emails:
            if email.value == value:
                return email
        raise AddressBookError("Email not found")
    
    def edit_email(self, old_value: str, new_value: str) -> None:
        if old_value == new_value:
            raise AddressBookError("New email must be different from old email")
        old_email = self.find_email(old_value)
        new_email = Email(new_value)
        index = self.emails.index(old_email)
        self.emails[index] = new_email

    def add_birthday(self, birthday: str) -> None:
        if self.birthday:
            raise AddressBookError("This contact already has a birthday date saved")
        self.birthday = Birthday(birthday)
    
    def remove_birthday(self) -> None:
        if not self.birthday:
            raise AddressBookError("Birthday not found")
        self.birthday = None

    def edit_birthday(self, value: str) -> None:
        if not self.birthday:
           raise AddressBookError("Birthday not found")
        self.birthday = Birthday(value)

    def add_address(self, value: str) -> None:
        if self.address:
            raise AddressBookError("Address already exists")
        self.address = Address(value)

    def remove_address(self) -> None:
        if not self.address:
            raise AddressBookError("Address not found")
        self.address = None

    def edit_address(self, value: str) -> None:
        if not self.address:
           raise AddressBookError("Address not found")
        self.address = Address(value)
    
    def __str__(self):
        return (
        f"[green]Name:[/green] [cyan]{self.name.value}[/cyan][green]; [/green]"
        f"[green]Phones:[/green] [cyan]{', '.join(p.value for p in self.phones) if self.phones else 'No phones'}[/cyan][green]; [/green]"
        f"[green]Emails:[/green] [cyan]{', '.join(e.value for e in self.emails) if self.emails else 'No emails'}[/cyan][green]; [/green]"
        f"[green]Birthday:[/green] [cyan]{self.birthday.date.strftime(Birthday.DATE_FORMAT) if self.birthday else 'No birthday'}[/cyan][green]; [/green]"
        f"[green]Address:[/green] [cyan]{self.address.value if self.address else 'No address'}[/cyan]"
    )

    def __repr__(self):
        return self.__str__()