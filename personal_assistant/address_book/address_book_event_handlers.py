import pickle
from ..shared import AddressBookError, catch_error, check_input
from . import AddressBook, Record

def format_record(record: Record) -> str:
    return str(record)


# Add a new contact to the dictionary
@catch_error
@check_input(min_args=1)
def add_contact(fields: dict[str], book: AddressBook)-> str:
    name = fields.get("name")
    record = book.find(name)

    # CASE 1: contact exists
    if record:
        # if no additional data
        if not fields:
            return "[red]Contact already exists, add something.[/red]\n" + format_record(record)
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
def change_phone(args, book: AddressBook) -> str:
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
@check_input(max_args=0)
def show_all(_, book: AddressBook) -> str:
    if not book:
        raise AddressBookError("No contacts saved.")

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
    from .address_book import AddressBook
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()