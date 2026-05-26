from .record_fields import Name, Phone, Birthday
from ...shared.error_handler.decorators.catch_error import ValueExistsError, NotFoundError

class Record():
    """Stores contact name and list of phones."""

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, value: str):
        if any(phone.value == value for phone in self.phones):
            raise ValueExistsError("This number already exists")
        self.phones.append(Phone(value))

    def remove_phone(self, value: str):
        phone = self.find_phone(value)
        self.phones.remove(phone)


    def edit_phone(self, old_number: str, new_number: str):
        if old_number == new_number:
            raise ValueExistsError("New phone must be different from old phone")
        old_phone = self.find_phone(old_number)
        new_phone = Phone(new_number)
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone

    def find_phone(self, value: str):
        for phone in self.phones:
            if phone.value == value:
                return phone
        raise NotFoundError("Phone not found")
    
    def add_birthday(self, birthday: str):
        if self.birthday:
            raise ValueExistsError("This contact already has a birthday date saved")
        self.birthday = Birthday(birthday)
    
    def __str__(self):
        return (
        f"[green]Name:[/green] [cyan]{self.name.value}[/cyan][green]; [/green]"
        f"[green]Phones:[/green] [cyan]{', '.join(p.value for p in self.phones) if self.phones else 'No phones'}[/cyan][green]; [/green]"
        f"[green]Birthday:[/green] [cyan]{self.birthday.date.strftime('%d.%m.%Y') if self.birthday else 'No birthday'}[/cyan]"
    )

    def __repr__(self):
        return self.__str__()