from .address_book import AddressBook
from .notes import Notes


class PersonalAssistant:
    def __init__(self):
        address_book = AddressBook()
        notes = Notes()

    def __getstate__(self):
        pass

    def __setstate__(self, state):
        pass     