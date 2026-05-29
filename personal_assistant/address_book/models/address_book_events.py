from enum import Enum


class AddressBookEvents(Enum):
    ADD_CONTACT = "add_contact"
    CHANGE_CONTACT = "change_contact"
    REMOVE_CONTACT = "remove_contact"
    SEARCH_CONTACT = "search_contact"
    UPCOMING = "show_upcoming_birthdays"
    SHOW_ALL = "show_all_contacts"
    
