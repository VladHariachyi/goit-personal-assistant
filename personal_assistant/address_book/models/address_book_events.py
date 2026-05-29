from enum import Enum


class AddressBookEvents(Enum):
    ADD_CONTACT = "add_contact"
    CHANGE_CONTACT = "change_contact"
    REMOVE_CONTACT = "remove_contact"
    SEARCH_CONTACT = "search_contact"
    SHOW_PHONE = "show_phone"
    REMOVE_PHONE = "remove_phone"
    SHOW_EMAIL = "show_email"
    REMOVE_EMAIL = "remove_email"
    SHOW_ADDRESS = "show_address"
    REMOVE_ADDRESS = "remove_address"
    SHOW_BIRTHDAY = "show_birthday"
    UPCOMING = "show_upcoming_birthdays"
    SHOW_ALL = "show_all_contacts"
    
