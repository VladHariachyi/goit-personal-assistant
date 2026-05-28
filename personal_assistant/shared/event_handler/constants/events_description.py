from ..models.address_book_events import AddressBookEvents
from ..models.notes_events import NotesEvents


AB_DESCRIPTIONS = {
    AddressBookEvents.ADD_CONTACT: "Create a new contact",
    AddressBookEvents.REMOVE_CONTACT: "Delete a contact",
    AddressBookEvents.SEARCH_CONTACT: "Search contact by name or phone",

    AddressBookEvents.ADD_PHONE: "Add phone number to contact",
    AddressBookEvents.CHANGE_PHONE: "Change existing phone number",
    AddressBookEvents.SHOW_PHONE: "Show all phone numbers for contact",
    AddressBookEvents.REMOVE_PHONE: "Remove phone number from contact",

    AddressBookEvents.ADD_EMAIL: "Add email to contact",
    AddressBookEvents.CHANGE_EMAIL: "Change contact email",
    AddressBookEvents.SHOW_EMAIL: "Show contact email",
    AddressBookEvents.REMOVE_EMAIL: "Remove email from contact",

    AddressBookEvents.ADD_ADDRESS: "Add address to contact",
    AddressBookEvents.CHANGE_ADDRESS: "Change contact address",
    AddressBookEvents.SHOW_ADDRESS: "Show contact address",
    AddressBookEvents.REMOVE_ADDRESS: "Remove contact address",

    AddressBookEvents.ADD_BIRTHDAY: "Add birthday to contact",
    AddressBookEvents.SHOW_BIRTHDAY: "Show contact birthday",
    AddressBookEvents.UPCOMING: "Show upcoming birthdays (next 7 days)",

    AddressBookEvents.SHOW_ALL: "Show all contacts",
}

NOTES_DESCRIPTIONS = {
    NotesEvents.ADD_NOTE: "Add new note",
    NotesEvents.ADD_TAG: "Add tag to note",
    NotesEvents.SEARCH_NOTE: "Search notes",
    NotesEvents.REMOVE_NOTE: "Remove note",
    NotesEvents.CHANGE_NOTE: "Change note content",
}