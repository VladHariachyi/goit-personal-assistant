from ..models import AddressBookEvents
from ..record.record_fields import Birthday


AB_DESCRIPTIONS = {
    AddressBookEvents.ADD_CONTACT: (
        'Adds a new contact to the address book. Provide the required "name" argument, '
        'which is used as the contact identifier. Example: add_contact <name="value"> '
        '\\[phone="value"] \\[email="value"] \\[birthday="value"] \\[address="value"]. '
        'Optional arguments are shown in square brackets `[]` for documentation purposes only. '
        'Do not include the brackets when entering the command.'
    ),
    AddressBookEvents.CHANGE_CONTACT: (
        'Changes an existing contact data. Provide the required "name" argument, '
        'which identifies the contact to update. Example: change_contact <name="value"> '
        '\\[new_name="value"] \\[phone="old=value,new=value"] \\[email="value"] '
        '\\[birthday="value"] \\[address="value"]. '
        'Optional arguments are shown in square brackets `[]` for documentation purposes only. '
        'Do not include the brackets when entering the command.'
    ),
    AddressBookEvents.REMOVE_CONTACT: (
        'Removes contact data or the entire contact. Provide the required "name" argument. '
        'Example: remove_contact <name="value"> '
        '\\[phone="value"] \\[email="value"] \\[birthday="value"] \\[address="value"]. '
        'Optional arguments are shown in square brackets `[]` for documentation purposes only. '
        'Do not include the brackets when entering the command.'
    ),
    AddressBookEvents.SEARCH_CONTACT: (
        'Searches contacts by given filters. At least one optional argument must be provided. '
        'Example: search_contact \\[name="value"] \\[phone="value"] \\[email="value"] '
        '\\[birthday="value"] \\[address="value"]. '
        'Optional arguments are shown in square brackets `[]` for documentation purposes only. '
        'Do not include the brackets when entering the command.'
    ),
    AddressBookEvents.UPCOMING: (
        'Shows upcoming birthdays within a number of days. Example: '
        'show_upcoming_birthdays \\[days="value"]. '
        'Optional arguments are shown in square brackets `[]` for documentation purposes only. '
        'Do not include the brackets when entering the command.'
    ),
    AddressBookEvents.SHOW_ALL: (
        'Displays all contacts in the address book. '
        'Usage: show_all_contacts. No arguments required.'
    ),
}

REQUIRED_PAIRS = [
    ("old_phone", "new_phone"),
    ("old_email", "new_email"),
    ("old_address", "new_address"),
    ("old_birthday", "new_birthday")
]

SEARCH_FILTERS = {
    "name": lambda r, q:
        q.lower() in r.name.value.lower(),
    "phone": lambda r, q:
        any(q in p.value for p in r.phones),
    "email": lambda r, q:
        any(q.lower() in e.value.lower() for e in r.emails),
    "birthday": lambda r, q:
        r.birthday is not None
        and q in r.birthday.date.strftime(Birthday.DATE_FORMAT),
    "address": lambda r, q:
        r.address is not None
        and q.lower() in r.address.value.lower(),
}