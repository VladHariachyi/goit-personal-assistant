from ..models import AddressBookEvents


AB_DESCRIPTIONS = {
    AddressBookEvents.ADD_CONTACT: "add_contact <name> \\[phone=value] \\[email=value] \\[birthday=value] \\[address=value]",
    AddressBookEvents.REMOVE_CONTACT: "remove_contact <name>",
    AddressBookEvents.SEARCH_CONTACT: "search <name|phone>",

    AddressBookEvents.CHANGE_PHONE: "change_phone <name> <old_phone> <new_phone>",
    AddressBookEvents.SHOW_PHONE: "show_phone <name>",
    AddressBookEvents.REMOVE_PHONE: "remove_phone <name> <phone>",

    AddressBookEvents.CHANGE_EMAIL: "change_email <name> <email>",
    AddressBookEvents.SHOW_EMAIL: "show_email <name>",
    AddressBookEvents.REMOVE_EMAIL: "remove_email <name> <email>",

    AddressBookEvents.CHANGE_ADDRESS: "change_address <name> <address>",
    AddressBookEvents.SHOW_ADDRESS: "show_address <name>",
    AddressBookEvents.REMOVE_ADDRESS: "remove_address <name>",

    AddressBookEvents.SHOW_BIRTHDAY: "show_birthday <name>",
    AddressBookEvents.UPCOMING: "birthdays [days]",

    AddressBookEvents.SHOW_ALL: "show_all",
}