from rich import print
from rich.console import Console
from rich.table import Table
from .address_book import (
    load_data,
    save_data,
    add_contact,
    change_contact,
    search_contact,
    remove_contact,
    show_all,
    birthdays,
    AddressBookEvents,
    AB_DESCRIPTIONS
)
from .notes import (
    Notes,
    NotesEvents,
    NOTES_DESCRIPTIONS,
    add_note,
    edit_note,
    remove_note
)
from .shared import parse_input

console = Console()


class PersonalAssistant:

    def __init__(self):
        self.notes = Notes()

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
        table.add_row("options", "Show all available commands")
        console.print(table)
        
        while True:
            user_input = input("Enter a command: ")
            command, params = parse_input(user_input)

            match command:
                case "exit" | "close":
                    save_data(book)
                    print("[green]Good bye![/green]")
                    break
                case "options":
                    self.show_options()
                    
                # --- ADDRESS BOOK ---
                case "add_contact":
                    print(add_contact(params, book))
                case "change_contact":
                    print(change_contact(params, book))
                case "remove_contact":
                    print(remove_contact(params, book))
                case "search_contact":
                    print(search_contact(params, book))
                case "show_upcoming_birthdays":
                    print(birthdays(params, book))
                case "show_all_contacts":
                    print(show_all(params, book))

                # --- NOTES ---
                case "add_note":
                    print(add_note(params, self.notes))
                case "search_note":
                    print("Search note - TODO")
                case "remove_note":
                    print(remove_note(params, self.notes))
                case "change_note":
                    print(edit_note(params, self.notes))

                # --- fallback ---
                case _:
                    print("[red]Invalid command.[/red]")
    
    def show_options(self):
        print('here')
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
        console.print(table)