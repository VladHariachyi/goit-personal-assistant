from ..models.address_book_events import AddressBookEvents
from ..models.notes_events import NotesEvents


def is_address_book_event(event: str) -> bool:
    try:
       found_event = AddressBookEvents(event)
       return bool(found_event)
    except ValueError:
        return False 

def is_notes_event(event: str) -> bool:
    try:
       found_event = NotesEvents(event)
       return bool(found_event)
    except ValueError:
        return False 