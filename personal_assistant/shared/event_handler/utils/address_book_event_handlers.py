import pickle
from typing import TYPE_CHECKING
from ...error_handler.decorators.catch_error import catch_error, ValueExistsError, NotFoundError
from ....address_book.record import Record


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
def add_contact(args, book: AddressBook)-> str:
    name, phone, *_ = args
    if book.phone_exists(phone):
        raise ValueExistsError("This phone already exists in another contact")
    
    record = book.find(name)

    if record is None:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return "[green]Contact added.[/green]"
    
    record.add_phone(phone)
    return "[green]Contact updated.[/green]"


# Change phone number for an existing contact
@catch_error
def change_contact(args, book: AddressBook) -> str:
    name, old_phone, new_phone, *_ = args
    record = book.find(name)

    if not record:
        raise KeyError
    
    record.edit_phone(old_phone, new_phone)
    return "[green]Contact updated.[/green]"


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
def show_all(book: AddressBook) -> str:
    if not book:
        raise NotFoundError("No contacts saved.")

    result = "\n".join(str(record) for record in book.values())
    return result


@catch_error
def add_birthday(args, book: AddressBook) -> str:
    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError
    record.add_birthday(birthday)
    return "[green]Birthday added[/green]"
    

@catch_error
def show_birthday(args, book: AddressBook) -> str:
    name, *_ = args
    record = book.find(name)

    if record is None:
        raise KeyError

    if record.birthday is None:
        raise NotFoundError("Birthday is not set")

    return f"[cyan]{record.birthday.date.strftime('%d.%m.%Y')}[/cyan]"
    

@catch_error
def birthdays(book: AddressBook) -> str:
    birthdays_list = book.get_upcoming_birthdays()
    result = []
    if not birthdays_list:
        return "The list is empty. No celebrations, only work!"
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