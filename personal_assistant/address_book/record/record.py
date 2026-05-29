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
    
    def change_name(self, new_name: str) -> None:
        self.name = Name(new_name)

    def validate_name_change(self, new_name: str) -> None:
        if self.name.value == new_name:
            raise AddressBookError("Nothing to update: names are identical.")

    def add_phone(self, value: str) -> None:
        if any(phone.value == value for phone in self.phones):
            raise AddressBookError("This phone number is already added to this contact. Please use a different number.")
        self.phones.append(Phone(value))

    def validate_phone_change(self, old_number: str, new_number: str) -> None:
        if not self.find_phone(old_number):
            raise AddressBookError("That phone number was not found in this contact. Please check it and try again.")
        if old_number == new_number:
            raise AddressBookError("It looks like the new phone number is the same as the old one. Please use a different number.")
        if new_number in [p.value for p in self.phones]:
            raise AddressBookError("New phone number is already in this contact. Please use a different one.")
        
    def change_phone(self, old_number: str, new_number: str) -> None:
        old_phone = self.find_phone(old_number)
        new_phone = Phone(new_number)
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone

    def remove_phone(self, value: str) -> None:
        phone = self.find_phone(value)
        self.phones.remove(phone)
    
    def find_phone(self, value: str) -> Phone:
        for phone in self.phones:
            if phone.value == value:
                return phone
        raise AddressBookError("That phone number was not found in this contact. Please check and try again.")
    
    def add_email(self, value: str) -> None:
        if any(email.value == value for email in self.emails):
            raise AddressBookError("It looks like this email is already added to this contact. Please use a different one.")
        self.emails.append(Email(value))

    def validate_email_change(self, old_value: str, new_value: str) -> None:
        if old_value not in [p.value for p in self.emails]:
            raise AddressBookError("It looks like this email was not found in this contact. Please check it and try again.")
        if old_value == new_value:
            raise AddressBookError("It looks like the new email is the same as the current one. Please use a different email.")
        if new_value in [p.value for p in self.emails]:
            raise AddressBookError("New email is already in this contact. Please use a different one.")
        
    def change_email(self, old_value: str, new_value: str) -> None:
        old_email = self.find_email(old_value)
        new_email = Email(new_value)
        index = self.emails.index(old_email)
        self.emails[index] = new_email

    def remove_email(self, value: str) -> None:
        email = self.find_email(value)
        self.emails.remove(email)

    def find_email(self, value: str) -> Email | None:
        for email in self.emails:
            if email.value == value:
                return email
        raise AddressBookError("It looks like this email was not found in this contact. Please check it and try again.")

    def add_birthday(self, birthday: str) -> None:
        if self.birthday:
            raise AddressBookError("This contact already has a birthday set. Please update it instead if needed.")
        self.birthday = Birthday(birthday)
    
    def validate_birthday_change(self, old_value: str, new_value: str)-> None:
        if not self.birthday:
           raise AddressBookError("It looks like this contact doesn't have a birthday set.")
        if self.birthday.date.strftime(Birthday.DATE_FORMAT) != old_value:
            raise AddressBookError("That old birthday doesn't match the current value. Please check it and try again.")
        if old_value == new_value:
            raise AddressBookError("It looks like the new birthday is the same as the current one. Please choose a different value.")
        
    def change_birthday(self, value: str) -> None:
        self.birthday = Birthday(value)

    def remove_birthday(self) -> None:
        if not self.birthday:
            raise AddressBookError("It looks like this contact doesn't have a birthday set.")
        self.birthday = None

    def add_address(self, value: str) -> None:
        if self.address:
            raise AddressBookError("This contact already has an address set.")
        self.address = Address(value)

    def validate_address_change(self,old_value:str, new_value: str)-> None:
        if not self.address:
           raise AddressBookError("This contact doesn't have an address set")
        if self.address.value != old_value:
            raise AddressBookError("That old address doesn't match the current value. Please check it and try again.")
        if self.address.value == new_value:
            raise AddressBookError("It looks like the new address is the same as the current one. Please enter a different address.")
    
    def change_address(self, value: str) -> None:
        self.address = Address(value)
   
    def remove_address(self) -> None:
        if not self.address:
            raise AddressBookError("This contact doesn't have an address to remove.")
        self.address = None

    def detailed_view(self):
        return (
            f"[green]Name:[/green] [cyan]{self.name.value}[/cyan]\n"
            f"[green]Phones:[/green] [cyan]{', '.join(p.value for p in self.phones) if self.phones else '-'}[/cyan]\n"
            f"[green]Emails:[/green] [cyan]{', '.join(e.value for e in self.emails) if self.emails else '-'}[/cyan]\n"
            f"[green]Birthday:[/green] [cyan]{self.birthday.date.strftime(Birthday.DATE_FORMAT) if self.birthday else '-'}[/cyan]\n"
            f"[green]Address:[/green] [cyan]{self.address.value if self.address else '-'}[/cyan]"
        )
    
    def __str__(self):
        phones = ", ".join(p.value for p in self.phones) if self.phones else "—"
        emails = ", ".join(e.value for e in self.emails) if self.emails else "—"
        birthday = (self.birthday.date.strftime(Birthday.DATE_FORMAT) if self.birthday else "—")
        address = self.address.value if self.address else "—"
        return (
            f"👤 [cyan]{self.name.value}[/cyan] | "
            f"[green]Phone:[/green] [cyan]{phones}[/cyan] | "
            f"[green]Email:[/green] [cyan]{emails}[/cyan] | "
            f"[green]Birthday:[/green] [cyan]{birthday}[/cyan] | "
            f"[green]Address:[/green] [cyan]{address}[/cyan]"
        )

    def __repr__(self):
        return self.__str__()