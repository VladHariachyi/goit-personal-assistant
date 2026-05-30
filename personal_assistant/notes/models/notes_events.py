from enum import Enum


class NotesEvents(Enum):
    ADD_NOTE = "add_note"
    SEARCH_NOTE = "search_note"
    REMOVE_NOTE = "remove_note"
    CHANGE_NOTE = "change_note"
