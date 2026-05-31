from rich import print
from rich.console import Console
from rich.table import Table
import pickle
from pathlib import Path

from .address_book import (
    AddressBook,
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
    remove_note,
    show_all_notes,
    search_note
)
from .shared import parse_input, Status, suggest_command, InputError, catch_error

console = Console()
default_pa_state_path = Path(__file__).parent.parent / "personal_assistant.pkl"


class PersonalAssistant:
    def __init__(self):
        self.notes = Notes()
        self.book = AddressBook()

    def __getstate__(self):
        """Generation the personal assistant current state which to be saved

        Returns:
        personal_assistant_state -- The current address book state
        """
        return {
            "notes": self.notes,
            "book": self.book
        }

    def __setstate__(self, state):
        """Retrieves the personal assistant state

        Arguments:
        personal_assistant_state -- The state which need to retreive 
        """
        if state:
            self.book = state.get("book", AddressBook())
            self.notes = state.get("notes", Notes())
            print(f"[green3]Personal assistant data is successfuly retreived[/green3]")
        else:
            print(f"[yellow1]Is not possible to retreive personal assistant state due to missed data [/yellow1]")

    def run(
        self,
        pa_state_path: Path
    ) -> None:
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
                    self.__save_state(pa_state_path)
                    break
                case "options":
                    self.show_options()
                    
                # --- ADDRESS BOOK ---
                case "add_contact":
                    print(add_contact(params, self.book))
                case "change_contact":
                    print(change_contact(params, self.book))
                case "remove_contact":
                    print(remove_contact(params, self.book))
                case "search_contact":
                    print(search_contact(params, self.book))
                case "show_upcoming_birthdays":
                    print(birthdays(params, self.book))
                case "show_all_contacts":
                    print(show_all(params, self.book))

                # --- NOTES ---
                case "add_note":
                    print(add_note(params, self.notes))
                case "change_note":
                    print(edit_note(params, self.notes))
                case "remove_note":
                    print(remove_note(params, self.notes))
                case "search_note":
                    print(search_note(params, self.notes))
                case "show_all_notes":
                    print(show_all_notes(self.notes))    

                # --- fallback ---
                case _:
                    print(guess_command(command))

    def __save_state(self, pa_state_path: Path):
        status = save_data(self, pa_state_path)
        message = None

        if status == Status.SUCCESS:
            message = (
                f"[gold1]The data is saved to '{pa_state_path}'.\n"
                f"Good bye! 👋[/gold1]"
                )
        else:
            message = (
                "[red]Is not possible to save data by provided path.\n"
                f"'{pa_state_path}', directory does not exist[/red]")
            
        print(message)
    
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
        console.print(table)


def save_data(
    personal_assistant: PersonalAssistant,
    path: Path
) -> Status:
    try: 
        with open(path, "wb") as f:
            pickle.dump(personal_assistant, f)
            return Status.SUCCESS
    except FileNotFoundError:
        return Status.ERROR


def start_personal_assistant(
    pa_state_path: Path = default_pa_state_path
) -> PersonalAssistant:
    personal_assistant: PersonalAssistant

    try:
        with open(pa_state_path, "rb") as f:
            personal_assistant = pickle.load(f)
    except FileNotFoundError:
        personal_assistant = PersonalAssistant()

    personal_assistant.run(pa_state_path)

    return personal_assistant


@catch_error
def guess_command(command: str) -> str:
    suggestion = suggest_command(command)
    if suggestion:
        return(f"[red]Unknown command [/red]'{command}'[red]. Did you mean [/red]'{suggestion}'[red]?[/red]")
    else:
        return(f"[red]Unknown command [/red]'{command}'[red]. Use 'options' to see commands.[/red]")