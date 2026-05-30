from ..shared import AddressBookError, catch_error, check_input, InputError
from . import AddressBook, Record
from .constants import REQUIRED_PAIRS, SEARCH_FILTERS

def format_record(record: Record) -> str:
    return str(record)

def validate_change_contact(fields: dict, pairs: list) -> None:
    for old, new in pairs:
        if old in fields or new in fields:
            if (old in fields) != (new in fields):
                raise InputError(f"Both {old} and {new} must be provided.")
            

# Add a new contact to the dictionary
@catch_error
@check_input(min_args=1)
def add_contact(fields: dict, book: AddressBook)-> str:
    
    name = fields.get("name")

    if not name:
        raise InputError(f"Invalid input. Name is required.")
    record = book.find(name)
    
    # ================= EXISTING CONTACT =================
    if record:
        # if no additional data
        if set(fields.keys()) == {"name"}:
            raise AddressBookError("Nothing to update. Please change at least one field.")
        # if phone provided -> update
        if "phone" in fields:
            phones = [p.strip() for p in fields["phone"].split(",")]
            for phone in phones:
                if book.phone_exists(phone):
                    raise AddressBookError("Phone already exists in your contacts.")
                record.add_phone(phone)
        
        if "email" in fields:
            emails = [p.strip() for p in fields["email"].split(",")]
            for email in emails:
                if book.email_exists(email):
                    raise AddressBookError("Email already exists in your contacts.")
                record.add_email(email)

        if "birthday" in fields:
            record.add_birthday(fields["birthday"])

        if "address" in fields:
            record.add_address(fields["address"])

        return "[green]Contact successfully updated.[/green]\n" + record.detailed_view()

    # ================= NEW CONTACT =================
    record = Record(name)

    if "phone" in fields:
        phone = fields["phone"]
        if book.phone_exists(phone):
            raise AddressBookError("Phone already exists in your contacts.")
        record.add_phone(phone)
    
    if "email" in fields:
        record.add_email(fields["email"])

    if "birthday" in fields:
        record.add_birthday(fields["birthday"])

    if "address" in fields:
        record.add_address(fields["address"])
        
    book.add_record(record)
    return "[green]Contact successfully added.[/green]\n" + record.detailed_view()


# Change phone number for an existing contact
@catch_error
@check_input(min_args=2)
def change_contact(fields: dict, book: AddressBook) -> str:
    name = fields.get("name")
    if not name:
        raise InputError("That command is missing a name. Try: change_contact name=<name> old_phone=<phone> new_phone=<phone>")
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
    for _, config in change_config.items():
        if config["field"] in fields:
            config["validate"]()

    # UPDATE
    for field_name, config in change_config.items():
        if config["field"] in fields:
            config["change"]()
            updated_fields.append(field_name)

    return f"[green]Contact updated successfully: {', '.join(updated_fields)}.[/green]\n" + record.detailed_view()


@catch_error
@check_input(min_args=1)
def search_contact(fields: dict, book: AddressBook) -> str:
    results = list(book.data.values())

    for field, query in fields.items():

        if field not in SEARCH_FILTERS:
            raise InputError(f"Unknown search field: {field}")

        results = [
            record for record in results
            if SEARCH_FILTERS[field](record, query)
        ]

    if not results:
        raise AddressBookError("No contacts found")

    return "\n".join(format_record(r) for r in results)


@catch_error
@check_input(min_args=1)
def remove_contact(fields: dict, book: AddressBook) -> str:
    if "name" not in fields:
        raise InputError("Name is required")

    name = fields["name"]
    record = book.find(name)

    if not record:
        raise AddressBookError("Contact not found")

    removed = []

    # =========================
    # DELETE WHOLE CONTACT
    # =========================
    if len(fields) == 1:
        book.delete(name)
        return f"Contact '{name}' removed"

    # =========================
    # DELETE PHONE
    # =========================
    if "phone" in fields:
        record.remove_phone(fields["phone"])
        removed.append("phone")

    # =========================
    # DELETE EMAIL
    # =========================
    if "email" in fields:
        record.remove_email(fields["email"])
        removed.append("email")

    # =========================
    # DELETE BIRTHDAY
    # =========================
    if "birthday" in fields:
        record.birthday = None
        removed.append("birthday")

    # =========================
    # DELETE ADDRESS
    # =========================
    if "address" in fields:
        record.address = None
        removed.append("address")

    if not removed:
        raise InputError("Nothing to remove")

    return f"Removed: {', '.join(removed)}"


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
@check_input(min_args=0, max_args=1)
def birthdays(args, book: AddressBook) -> str:
    requested_days = int(args[0]) if args else 7
    birthdays_list = book.get_upcoming_birthdays(requested_days)
    result = []
    if not birthdays_list:
        return "[green]No upcoming birthdays. Quiet times ahead 😊[/green]"
    for user in birthdays_list:
        result.append(
            f"Name: [cyan]{user['name']}[/cyan], congratulation date: [cyan]{user['congratulation_date']}[/cyan]"
        )
    return "\n".join(result)
