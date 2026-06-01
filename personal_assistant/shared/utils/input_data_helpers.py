import re
from difflib import get_close_matches

COMMANDS = [
    "exit",
    "options",
    "add_contact",
    "change_contact",
    "remove_contact",
    "search_contact",
    "show_upcoming_birthdays",
    "show_all_contacts",
    "add_note",
    "change_note",
    "remove_note",
    "search_note",
    "show_all_notes"  
]

def parse_input(user_input: str) -> tuple[str, dict]:
    parsed_params = {}
    if not user_input.strip():
        return ("", {}) 
    input_pattern = r"\w+=[\"\']{1}[^\"\']+[\"\']{1}"
    params = re.findall(input_pattern, user_input)

    for param in params:
        key, val = param.split("=", 1)
        parsed_params[key.strip().lower()] = val.strip().strip("\"'")

    command = user_input.split()[0].lower()

    return (command, parsed_params)

def suggest_command(user_command: str) -> str | None:
    matches = get_close_matches(user_command, COMMANDS, n=1, cutoff=0.6)
    return matches[0] if matches else None