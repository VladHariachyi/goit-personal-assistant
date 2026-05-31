from collections import UserList

from .note import Note
from ..shared.error_handler import NotesError

class Notes(UserList):
    def add_note(
        self,
        new_note: Note
    ) -> None:
        is_exist = bool(len([note for note in self.data if note.title == new_note.title]))

        if is_exist:
            raise NotesError("The note is already exist, add a new one")

        self.data.append(new_note)
    
    def delete_note(self, note_title: str) -> None:
        note_index = self.__get_note_index(note_title)

        self.data.pop(note_index)

    def get_note_by_title(self, note_title: str) -> Note | None:
        note_index = self.__get_note_index(note_title, False)

        return None if note_index is None else self.data[note_index]

    def find_notes(
        self, 
        note_title: str = "", 
        note_description: str = "", 
        note_tag: str = ""
    ) -> list[Note] | None:
        if note_title:
            return [note for note in self.data if note_title.lower() in note.title.value.lower()]
        
        if note_description:
            return [note for note in self.data if len(note.find_descriptions(note_description))]
        
        if note_tag:
            return [note for note in self.data if len(note.find_tags(note_tag))]

    def __get_note_index(
        self, 
        note_title: str,
        throw_error_if_not_found: bool = True
    ) -> int | None:
        found_note_index = None

        try:
           found_note_index = [note.title.value.lower() for note in self.data].index(note_title.lower()) 
        except ValueError:
            if throw_error_if_not_found:
                raise NotesError(f"The note is not found by title: '{note_title}'")
        
        return found_note_index