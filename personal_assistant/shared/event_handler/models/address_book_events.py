from enum import Enum


class AddressBookEvents(Enum):
    ADD_CONTACT = "ab_add_contact"
    REMOVE_CONTACT = "ab_remove_contact"
    SEARCH_CONTACT = "ab_search_contact"
    ADD_PHONE = "ab_add_phone"
    CHANGE_PHONE = "ab_change_phone"
    SHOW_PHONE = "ab_show_phone"
    REMOVE_PHONE = "ab_remove_phone"
    ADD_EMAIL = "ab_add_email"
    CHANGE_EMAIL = "ab_change_email"
    SHOW_EMAIL = "ab_show_email"
    REMOVE_EMAIL = "ab_remove_email"
    ADD_ADDRESS = "ab_add_address"
    CHANGE_ADDRESS = "ab_change_address"
    SHOW_ADDRESS = "ab_show_address"
    REMOVE_ADDRESS = "ab_remove_address"
    ADD_BIRTHDAY = "ab_add_birthday"
    SHOW_BIRTHDAY = "ab_show_birthday"
    UPCOMING = "ab_show_upcoming_birthdays"
    SHOW_ALL = "ab_show_all_contacts"
