import pickle
from typing import TYPE_CHECKING
from ...error_handler.decorators.catch_error import catch_error, ValueExistsError, NotFoundError

if TYPE_CHECKING:
    from ....address_book.address_book import AddressBook
    from ....address_book.record import Record

# Parse user input into command and arguments
def parse_input(user_input):
    parts = user_input.split()

    if not parts:
        return "", []
    
    cmd, *args = parts
    cmd = cmd.strip().lower()
    return cmd, *args


# Add a new contact to the dictionary
@catch_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    if book.phone_exists(phone):
        raise ValueExistsError("This phone already exists in another contact")
    
    record = book.find(name)

    if record is None:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        # return SUCCESS + "Contact added."
        return "Contact added."
    
    record.add_phone(phone)
    # return SUCCESS + "Contact updated."
    return "Contact updated."


# Change phone number for an existing contact
@catch_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)

    if not record:
        raise KeyError
    
    # record.find_phone(old_phone)
    record.edit_phone(old_phone, new_phone)
    # return SUCCESS + "Contact updated."
    return "Contact updated."


# Show phone number for a specific contact
@catch_error
def show_phone(args, book: AddressBook):
    name = args[0]
    record = book.find(name)

    if record is None:
        raise KeyError
    
    phones = [p.value for p in record.phones]
    # return INFO + ", ".join(phones)
    return ", ".join(phones)

# Show all saved contacts
@catch_error
def show_all(book: AddressBook):
    if not book:
        raise NotFoundError("No contacts saved.")

    result = "\n".join(str(record) for record in book.values())
    return result

@catch_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError
    record.add_birthday(birthday)
    # return SUCCESS + "Birthday added"
    return "Birthday added"
    

@catch_error
def show_birthday(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)

    if record is None:
        raise KeyError

    if record.birthday is None:
        raise NotFoundError("Birthday is not set")

    # return INFO + record.birthday.date.strftime("%d.%m.%Y")
    return record.birthday.date.strftime("%d.%m.%Y")
    

@catch_error
def birthdays(book: AddressBook):
    birthdays_list = book.get_upcoming_birthdays()
    result = []
    for user in birthdays_list:
        result.append(
            # f"Name: {INFO + user['name'] + RESET}, congratulation date: {INFO + user['congratulation_date'] + RESET}"
            f"Name: {user['name']}, congratulation date: {user['congratulation_date']}"
        )
    return "\n".join(result)


@catch_error
def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    from ....address_book.address_book import AddressBook
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()