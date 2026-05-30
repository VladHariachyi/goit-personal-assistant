from ..models import AddressBookEvents
from ..record.record_fields import Birthday


AB_DESCRIPTIONS = {
    AddressBookEvents.ADD_CONTACT: 'add_contact <name="value"> \\[phone="value"] \\[email="value"] \\[birthday="value"] \\[address="value"]',
    AddressBookEvents.CHANGE_CONTACT: 'change_contact <name="value"> \\[new_name="value"] .... \\[old_phone="value" new_phone="value"]...',
    AddressBookEvents.REMOVE_CONTACT: 'remove_contact <name="value"> \\[phone="value"] \\[email="value"] \\[birthday="value"] \\[address="value"]',
    AddressBookEvents.SEARCH_CONTACT: 'search_contact \\[name="value"] \\[phone="value"] \\[email="value"] \\[birthday="value"] \\[address="value"]',

    AddressBookEvents.UPCOMING: 'show_upcoming_birthdays \\[days="value"]',

    AddressBookEvents.SHOW_ALL: "show_all_contacts",
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