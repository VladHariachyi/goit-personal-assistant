from .address_book.address_book import AddressBook
from .notes import Notes
from .shared.event_handler.utils import (
    parse_input, 
    add_contact, 
    change_contact, 
    show_phone, 
    show_all, 
    add_birthday, 
    show_birthday, 
    birthdays,
    load_data,
    save_data,
)
from rich import print


class PersonalAssistant:
    def __init__(self):
        self.address_book = load_data()
        self.notes = Notes()

    def __getstate__(self):
        pass

    def __setstate__(self, state):
        pass     

    def run(self):
        book = self.address_book
        # print(SUCCESS + "Welcome to the assistant bot!")
        print("Welcome to the assistant bot!")
        
        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            match command:
                case "close" | "exit":
                    save_data(book)
                    # print(SUCCESS + "Good bye!")
                    print("Good bye!")
                    break
                case "hello":
                    # print(SUCCESS + "How can I help you?")
                    print("How can I help you?")
                case "add":
                    print(add_contact(args, book))
                case "change":
                    print(change_contact(args, book))
                case "phone":
                    print(show_phone(args, book))
                case "all":
                    print(show_all(book))
                case "add-birthday":
                    print(add_birthday(args, book))
                case "show-birthday":
                    print(show_birthday(args, book))
                case "birthdays":
                    print(birthdays(book))
                case _:
                    # print(ERROR + "Invalid command.")
                    print("Invalid command.")