from .notes import Notes
from .shared.event_handler.utils import (
    parse_input, 
    load_data,
    save_data,
    add_contact,
    change_phone,
    show_phone,
    show_all,
    add_birthday,
    show_birthday,
    birthdays,
)
from rich import print
from rich.console import Console
from rich.table import Table
from .shared.event_handler.models import AddressBookEvents, NotesEvents, AB_DESCRIPTIONS, NOTES_DESCRIPTIONS


class PersonalAssistant:

    def __init__(self):
        self.notes = Notes()
        self.console = Console()

    def run(self) -> None:
        book = load_data()
        table = Table(
            title="[bold green]Welcome to the assistant bot![/bold green]",
            show_lines=True
        )
        table.add_column("Command", style="cyan")
        table.add_column("Description", style="white")

        # --- MAIN MENU---
        table.add_row("exit / close", "Exit the program")
        table.add_row("hello", "Show greeting message")
        table.add_row("options", "Show all available commands")
        self.console.print(table)
        
        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            match command:
                case "exit" | "close":
                    save_data(book)
                    print("[green]Good bye![/green]")
                    break
                case "hello":
                    print("[green]How can I help you?[/green]")
                case "options":
                    self.show_options()
                # --- ADDRESS BOOK ---
                case "add_contact":
                    print(add_contact(args, book))
                case "remove_contact":
                    print("Remove contact - TODO")
                case "search_contact":
                    print("Search contact - TODO")
                case "change_phone":
                    print(change_phone(args, book))
                case "show_phone":
                    print(show_phone(args, book))
                case "remove_phone":
                    print("Remove phone - TODO")
                case "add_email":
                    print("Add email - TODO")
                case "change_email":
                    print("Change email - TODO")
                case "show_email":
                    print("Show email - TODO")
                case "remove_email":
                    print("Remove email - TODO")
                case "add_address":
                    print("Add address - TODO")
                case "change_address":
                    print("Change address - TODO")
                case "show_address":
                    print("Show address - TODO")
                case "remove_address":
                    print("Remove address - TODO")
                case "add_birthday":
                    print(add_birthday(args, book))
                case "show_birthday":
                    print(show_birthday(args, book))
                case "show_upcoming_birthdays":
                    print(birthdays(args, book))
                case "show_all_contacts":
                    print(show_all(book))

                # --- NOTES ---
                case "add_note":
                    print("Add note - TODO")
                case "add_tag":
                    print("Add tag - TODO")
                case "search_note":
                    print("Search note - TODO")
                case "remove_note":
                    print("Remove note - TODO")
                case "change_note":
                    print("Change note - TODO")

                # --- fallback ---
                case _:
                    print("[red]Invalid command.[/red]")
    
    def show_options(self):
        table = Table(title="Available commands", show_lines=True)
        table.add_column("Command", style="cyan")
        table.add_column("Usage", style="white")

        # --- ADDRESS BOOK ---
        table.add_row("📒 Address Book", "", style="bold yellow")
        for event in AddressBookEvents:
            table.add_row(
                event.value,
                AB_DESCRIPTIONS.get(event, "")
            )

        # --- NOTES ---
        table.add_row("📝 Notes", "", style="bold yellow")

        for event in NotesEvents:
            table.add_row(
                event.value,
                NOTES_DESCRIPTIONS.get(event, "")
            )
        self.console.print(table)