from enum import Enum


class AddressBookEvents(Enum):
    ADD_CONTACT = "add_contact"
    REMOVE_CONTACT = "remove_contact"
    SEARCH_CONTACT = "search_contact"
    CHANGE_PHONE = "change_phone"
    SHOW_PHONE = "show_phone"
    REMOVE_PHONE = "remove_phone"
    ADD_EMAIL = "add_email"
    CHANGE_EMAIL = "change_email"
    SHOW_EMAIL = "show_email"
    REMOVE_EMAIL = "remove_email"
    ADD_ADDRESS = "add_address"
    CHANGE_ADDRESS = "change_address"
    SHOW_ADDRESS = "show_address"
    REMOVE_ADDRESS = "remove_address"
    ADD_BIRTHDAY = "add_birthday"
    SHOW_BIRTHDAY = "show_birthday"
    UPCOMING = "show_upcoming_birthdays"
    SHOW_ALL = "show_all_contacts"
    
