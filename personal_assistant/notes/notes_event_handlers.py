from ..shared import NotesError, catch_error, check_input, check_input
from .note import Note
from .notes import Notes


def add_note_props(note: Note, props: dict[str, str]) -> None:
    for prop, value in props.items():
        if (prop == "description"):
            note.add_description(value)

        if (prop == "tag"):
            note.add_tag(value)
    

@catch_error
@check_input(min_args=1)
def add_note(fields: dict[str], notes: Notes) -> str:
    fields_lenght = len(fields.keys())
    note_title = fields.get("title")
    note = notes.get_note_by_title(note_title)
    # check args
    has_single_title_arg = note_title and fields_lenght == 1
    has_multiple_args = note_title and fields_lenght > 1
    # conditions
    is_exist_with_title_arg = note and has_single_title_arg
    is_exist_with_multiple_args = note and has_multiple_args 
    is_not_exist_with_title_arg = not note and has_single_title_arg
    is_not_exist_with_multiple_args = not note and has_multiple_args

    if is_exist_with_title_arg:
        raise NotesError(f"Note already exists\n{str(note)}")
    
    if is_not_exist_with_title_arg:
        note = Note(note_title)
        notes.add_note(note)

        return f"[green]Note added.[/green]\n{str(note)}"

    if is_exist_with_multiple_args:
        del fields["title"]

        add_note_props(note, fields)

        return f"[green]Note is updated.[/green]\n{str(note)}"
    
    if is_not_exist_with_multiple_args:
        del fields["title"]

        note = Note(note_title)

        add_note_props(note, fields)
        notes.add_note(note)

        return f"[green]Note added.[/green]\n{str(note)}"
