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

    def run(self) -> None:
        book = self.address_book
        print("[green]Welcome to the assistant bot![/green]")
        
        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            match command:
                case "close" | "exit":
                    save_data(book)
                    print("[green]Good bye![/green]")
                    break
                case "hello":
                    print("[green]How can I help you?[/green]")
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
                    print("[red]Invalid command.[/red]")