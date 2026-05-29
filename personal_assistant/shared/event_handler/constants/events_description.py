from ..models.address_book_events import AddressBookEvents
from ..models.notes_events import NotesEvents


AB_DESCRIPTIONS = {
    AddressBookEvents.ADD_CONTACT: "add_contact <name=value> \\[phone=value] \\[email=value] \\[birthday=value] \\[address=value]",
    AddressBookEvents.CHANGE_CONTACT: "change_contact <name=value> \\[new_name=value] .... \\[old_phone=value new_phone=value]...",
    AddressBookEvents.REMOVE_CONTACT: "remove_contact <name>",
    AddressBookEvents.SEARCH_CONTACT: "search <name|phone>",

    AddressBookEvents.SHOW_PHONE: "show_phone <name>",
    AddressBookEvents.REMOVE_PHONE: "remove_phone <name> <phone>",

    AddressBookEvents.SHOW_EMAIL: "show_email <name>",
    AddressBookEvents.REMOVE_EMAIL: "remove_email <name> <email>",

    AddressBookEvents.SHOW_ADDRESS: "show_address <name>",
    AddressBookEvents.REMOVE_ADDRESS: "remove_address <name>",

    AddressBookEvents.SHOW_BIRTHDAY: "show_birthday <name>",
    AddressBookEvents.UPCOMING: "birthdays [days]",

    AddressBookEvents.SHOW_ALL: "show_all",
}

NOTES_DESCRIPTIONS = {
    NotesEvents.ADD_NOTE: "add_note <text>",
    NotesEvents.CHANGE_NOTE: "change_note <id> <text>",
    NotesEvents.REMOVE_NOTE: "remove_note <id>",

    NotesEvents.ADD_TAG: "add_tag <id> <tag>",
    NotesEvents.SEARCH_NOTE: "search_note <text|tag>",
}

REQUIRED_PAIRS = [
    ("old_phone", "new_phone"),
    ("old_email", "new_email"),
    ("old_address", "new_address"),
    ("old_birthday", "new_birthday")
]