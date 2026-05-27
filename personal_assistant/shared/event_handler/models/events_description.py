from .address_book_events import AddressBookEvents
from .notes_events import NotesEvents

AB_DESCRIPTIONS = {
    AddressBookEvents.ADD_CONTACT: "add_contact <name> [field=value]",
    AddressBookEvents.REMOVE_CONTACT: "remove_contact <name>",
    AddressBookEvents.SEARCH_CONTACT: "search <name|phone>",

    AddressBookEvents.CHANGE_PHONE: "change_phone <name> <old_phone> <new_phone>",
    AddressBookEvents.SHOW_PHONE: "show_phone <name>",
    AddressBookEvents.REMOVE_PHONE: "remove_phone <name> <phone>",

    AddressBookEvents.ADD_EMAIL: "add_email <name> <email>",
    AddressBookEvents.CHANGE_EMAIL: "change_email <name> <email>",
    AddressBookEvents.SHOW_EMAIL: "show_email <name>",
    AddressBookEvents.REMOVE_EMAIL: "remove_email <name> <email>",

    AddressBookEvents.ADD_ADDRESS: "add_address <name> <address>",
    AddressBookEvents.CHANGE_ADDRESS: "change_address <name> <address>",
    AddressBookEvents.SHOW_ADDRESS: "show_address <name>",
    AddressBookEvents.REMOVE_ADDRESS: "remove_address <name>",

    AddressBookEvents.ADD_BIRTHDAY: "add_birthday <name> <DD.MM.YYYY>",
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