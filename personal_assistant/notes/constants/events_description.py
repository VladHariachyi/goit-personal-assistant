from ..models import NotesEvents


NOTES_DESCRIPTIONS = {
    NotesEvents.ADD_NOTE: (
        'Adds a new note. Provide the required "title" argument, which is used as both ' 
        'the note title and its unique identifier. Exampe:  add_note <title="value"> '
        '\\[description="value"] \\[tag="#value"]. Optional arguments are shown in square brackets `[]` '
        'for documentation purposes only. Do not include the brackets when entering the command.'
    ),
    NotesEvents.CHANGE_NOTE: (
        'Changes the exisitng note content. Provide the required "title" argument, '
        'which is used as both the note title and its unique identifier.'
        'Exampe: change_note <title="Old title"> \\[new_title="New title"] \\[description="Old description"] '
        '\\[new_description="New description"] \\[tag="#old_tag"] \\[new_tag="#new_tag"] '
        'Optional arguments are shown in square brackets `[]` '
        'for documentation purposes only. Do not include the brackets when entering the command.'
    ),
    NotesEvents.REMOVE_NOTE: (
        'Removes note existing content or note itself. Provide the required "title" argument, which '
        'is note unique identifier. Example remove_note <title="value"> \\[description="value"] \\[tag="#value"] '
        'Optional arguments are shown in square brackets `[]` '
        'for documentation purposes only. Do not include the brackets when entering the command.'
    ),
}