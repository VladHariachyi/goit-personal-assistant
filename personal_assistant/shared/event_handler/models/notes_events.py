from enum import Enum


class NotesEvents(Enum):
    ADD_NOTE = "nt_add_note"
    ADD_TAG = "nt_add_tag"
    SEARCH_NOTE = "nt_search_note"
    REMOVE_NOTE = "nt_remove_note"
    CHANGE_NOTE = "nt_change_note"
