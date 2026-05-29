import pickle
from typing import TYPE_CHECKING
from ....shared import AddressBookError, catch_error, check_input, InputError
from ....address_book.record import Record
from ....address_book.record.record_fields import Birthday
from .helpers import format_record, parse_contact_fields, validate_change_contact
from ..constants import REQUIRED_PAIRS
from datetime import datetime


if TYPE_CHECKING:
    from ....address_book.address_book import AddressBook


# Parse user input into command and arguments
def parse_input(user_input) -> tuple[str, ...]:
    parts = user_input.split()

    if not parts:
        return "", []
    
    cmd, *args = parts
    cmd = cmd.strip().lower()
    return cmd, *args


# Add a new contact to the dictionary
@catch_error
@check_input(min_args=1)
def add_contact(args, book: AddressBook)-> str:
    fields = parse_contact_fields(args)

    if not "name" in fields:
        raise InputError(f"Incorrect input. Please use 'options' to see available commands and correct format.")
    
    name = fields["name"]
    record = book.find(name)
    
    # CASE 1: contact exists
    if record:
        # if no additional data
        if not any(key != "name" for key in fields):
            raise AddressBookError("Contact already exists, add something.\n"+ format_record(record))
        # if phone provided -> update
        if "phone" in fields:
            phone = fields["phone"]
            if book.phone_exists(phone):
                raise AddressBookError("This phone number already exists")
            record.add_phone(phone)
        
        if "email" in fields:
            record.add_email(fields["email"])

        if "birthday" in fields:
            record.add_birthday(fields["birthday"])

        if "address" in fields:
            record.add_address(fields["address"])

        return "[green]Contact updated.[/green]\n" + format_record(record)

    # CASE 2: contact does not exist
    record = Record(name)

    # CASE 2.1: with phone
    if "phone" in fields:
        phone = fields["phone"]
        if book.phone_exists(phone):
            raise AddressBookError("This phone number already exists")
        record.add_phone(phone)
    
    if "email" in fields:
        record.add_email(fields["email"])

    if "birthday" in fields:
        record.add_birthday(fields["birthday"])

    if "address" in fields:
        record.add_address(fields["address"])
        
    book.add_record(record)
    return "[green]Contact added.[/green]\n" + format_record(record)


# Change phone number for an existing contact
@catch_error
@check_input(min_args=2)
def change_contact(args, book: AddressBook) -> str:
    fields = parse_contact_fields(args)
    if "name" not in fields:
        raise InputError("Name is required. Use: change_contact name=<name> ...")
    name = fields["name"]
    record = book.find(name)

    if not record:
        raise AddressBookError("Contact doesn't exist, please create the contact first.")
    
    validate_change_contact(fields, REQUIRED_PAIRS)
    updated_fields = []

    change_config = {
        "name": {
            "field": "new_name",
            "validate": lambda: record.validate_name_change(fields["new_name"]),
            "change": lambda: (record.change_name(fields["new_name"]),book.rename_record(name, fields["new_name"])),
        },
        "phone": {
            "field": "new_phone",
            "validate": lambda: record.validate_phone_change(fields["old_phone"],fields["new_phone"]),
            "change": lambda: record.change_phone(fields["old_phone"],fields["new_phone"]),
        },
        "email": {
            "field": "new_email",
            "validate": lambda: record.validate_email_change(fields["old_email"],fields["new_email"]),
            "change": lambda: record.change_email(fields["old_email"],fields["new_email"]),
        },
        "birthday": {
            "field": "new_birthday",
            "validate": lambda: record.validate_birthday_change(fields["old_birthday"],fields["new_birthday"]),
            "change": lambda: record.change_birthday(fields["new_birthday"]),
        },
        "address": {
            "field": "new_address",
            "validate": lambda: record.validate_address_change(fields["old_address"],fields["new_address"]),
            "change": lambda: record.change_address(fields["new_address"]),
        },
    }

    # VALIDATION
    for field_name, config in change_config.items():
        if config["field"] in fields:
            config["validate"]()

    # UPDATE
    for field_name, config in change_config.items():
        if config["field"] in fields:
            config["change"]()
            updated_fields.append(field_name)

    return f"[green]Contact updated successfully: {', '.join(updated_fields)}.[/green]\n" + format_record(record)


# Show phone number for a specific contact
@catch_error
def show_phone(args, book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)

    if record is None:
        raise KeyError
    
    phones = [p.value for p in record.phones]
    return f"[cyan]{', '.join(phones)}[/cyan]"


# Show all saved contacts
@catch_error
@check_input(max_args=0)
def show_all(_, book: AddressBook) -> str:
    if not book:
        raise AddressBookError("No contacts saved.")

    result = "\n".join(str(record) for record in book.values())
    return result
    

@catch_error
def show_birthday(args, book: AddressBook) -> str:
    name, *_ = args
    record = book.find(name)

    if record is None:
        raise KeyError

    if record.birthday is None:
        raise AddressBookError("Birthday is not set")

    return f"[cyan]{record.birthday.date.strftime('%d.%m.%Y')}[/cyan]"
    

@catch_error
@check_input(min_args=0, max_args=1)
def birthdays(args, book: AddressBook) -> str:
    requested_days = int(args[0]) if args else 7
    birthdays_list = book.get_upcoming_birthdays(requested_days)
    result = []
    if not birthdays_list:
        return "[green]The list is empty. No celebrations, only work![/green]"
    for user in birthdays_list:
        result.append(
            f"Name: [cyan]{user['name']}[/cyan], congratulation date: [cyan]{user['congratulation_date']}[/cyan]"
        )
    return "\n".join(result)


@catch_error
def save_data(book, filename="addressbook.pkl") -> None:
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl") -> AddressBook:
    from ....address_book.address_book import AddressBook
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()