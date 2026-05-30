from ..shared import NotesError, catch_error, check_input
from .note import Note
from .notes import Notes


def add_note_props(note: Note, props: dict[str, str]) -> None:
    for prop, value in props.items():
        if (prop == "description"):
            note.add_description(value)

        if (prop == "tag"):
            note.add_tag(value)
    

@catch_error
@check_input(min_args=1, max_args=3)
def add_note(fields: dict, notes: Notes) -> str | None:
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

    if not note_title:
        raise NotesError(f"The note title is not provided")

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

        return f"[green]Note added.[/green]\n {str(note)}"


@catch_error
@check_input(min_args=2, max_args=6)
def edit_note(fields: dict, notes: Notes) -> str:
    note_title = fields.get("title")
    note = notes.get_note_by_title(note_title)

    if not note:
        raise NotesError(f"The note does not exist")

    new_note_title = fields.get("new_title")
    note_description = fields.get("description")
    new_note_description = fields.get("new_description")
    note_tag = fields.get("tag")
    new_note_tag = fields.get("new_tag")

    if note_title and new_note_title:
        note.edit_title(new_note_title)

    if note_description and new_note_description:
        note.edit_description(note_description, new_note_description)

    if note_tag and new_note_tag:
        note.edit_tag(note_tag, new_note_tag)

    return f"[green]Note is updated.[/green]\n{str(note)}"
       
    
@catch_error
@check_input(min_args=1)
def remove_note(fields: dict, notes: Notes) -> str:
    note_title = fields.get("title")
    note = notes.get_note_by_title(note_title)
    fields_lenght = len(fields.keys())

    if not note:
        raise NotesError(f"The note does not exist")
    
    if fields_lenght == 1:
        notes.delete_note(note_title)
        return f"[green]Note is removed.[/green]"
        
    description = fields.get("description")
    tag = fields.get("tag")
    is_description_removed = False
    is_tag_removed = False
    message = ""

    if description:
        note.remove_description(description)
        is_description_removed = True

    if tag:
        note.remove_tag(tag)
        is_tag_removed = True


    if is_description_removed and is_tag_removed:
        message = "Note description and tag are removed"
    elif is_description_removed:
        message = "Note description is removed"
    elif is_tag_removed:
        message = "Note tag is removed"
    else:
        raise NotesError(f"The note can't be removed")


    return f"[green]{message}.[/green]\n{str(note)}"


@catch_error
@check_input(min_args=1)
def search_note(fields: dict, notes: Notes) -> str:

    title = fields.get("title")
    tag = fields.get("tag")

    found_notes = []

    if title:
        found_notes = notes.find_notes(
            note_title=title
        )

    elif tag:
        found_notes = notes.find_notes(
            note_tag=tag
        )

    else:
        raise NotesError(
            "Please provide title or tag"
        )

    if not found_notes:
        raise NotesError(
            "No notes found"
        )

    return "\n\n".join(
        str(note)
        for note in found_notes
    )

@catch_error
def show_all_notes(notes: Notes) -> str:

    if not notes.data:
        raise NotesError(
            "There are no notes"
        )

    return "\n\n".join(
        str(note)
        for note in notes.data
    )
