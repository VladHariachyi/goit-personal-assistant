from .utils import is_address_book_event, is_notes_event


def handle_address_book_event(event: str, *args):
    pass

def handle_notes_event(event: str, *args):
    pass

def handle_event(event: str, *args):
    if (is_address_book_event(event)):
        handle_address_book_event(event, *args)
        return
    
    if (is_notes_event(event)):
        handle_notes_event(event, *args)
        return