from ..models import NotesEvents


NOTES_DESCRIPTIONS = {
    NotesEvents.ADD_NOTE: "add_note <text>",
    NotesEvents.CHANGE_NOTE: "change_note <id> <text>",
    NotesEvents.REMOVE_NOTE: "remove_note <id>",

    NotesEvents.ADD_TAG: "add_tag <id> <tag>",
    NotesEvents.SEARCH_NOTE: "search_note <text|tag>",
}