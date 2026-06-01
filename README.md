# 🤖 Personal Assistant CLI

A command-line personal assistant for managing contacts and notes, with persistent storage between sessions.
This project can be used both as a script and as an installed CLI package.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [Usage Guide](#usage-guide)
  - [Address Book Commands](#address-book-commands)
  - [Notes Commands](#notes-commands)
  - [General Commands](#general-commands)
- [Input Format](#input-format)
- [Data Persistence](#data-persistence)
- [Project Structure](#project-structure)
- [Developer Documentation](#developer-documentation)

---

## Features

- **Address Book** — add, update, search, and remove contacts with phones, emails, birthdays, and addresses
- **Notes** — create, tag, search, edit, and delete notes
- **Upcoming Birthdays** — list contacts with birthdays in the next N days
- **Persistent Storage** — data is automatically saved on exit and restored on next launch
- **Rich Terminal Output** — color-coded, table-formatted output via the `rich` library

---

## Requirements

- Python 3.10+
- pip

---

## Installation

```bash
# 1. Clone the repository
git clone <repository-url>
cd goit-personal-assistant

# 2. (Recommended) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

---

### CLI Installation (optional)

After cloning the repository, navigate into the project folder:

```bash
cd goit-personal-assistant
```
After installing the project as a package, you can run it globally:

```bash
pip install -e .
assistant
```

---

## Running the App

```bash
# Run as script
python main.py

# OR run as installed CLI command
assistant
```

On first launch, a new empty assistant is created. On subsequent launches, your saved data is automatically restored from `personal_assistant.pkl` in the project root.

---

## Usage Guide

When the assistant starts, it shows a welcome table with the two basic commands. Type `options` at any time to see the full list of available commands.

### Input Format

All commands use a `key="value"` argument syntax:

```
command_name key1="value1" key2="value2"
```

- Values must be wrapped in single or double quotes.
- Argument order does not matter.
- Optional arguments are noted with `[square brackets]` in the `options` table — do **not** include the brackets when typing the command.

---

### Address Book Commands

#### `add_contact`

Adds a new contact or updates an existing one.

```
add_contact name="John Doe"
add_contact name="John Doe" phone="+380991234567" email="john@example.com"
add_contact name="John Doe" birthday="25.12.1990" address="Baker Street 221B"
```

- **`name`** — required; serves as the unique identifier
- **`phone`** — Ukrainian format: `+380XXXXXXXXX`
- **`email`** — standard email format: `name@domain.com`
- **`birthday`** — format: `DD.MM.YYYY`
- **`address`** — free text, must contain at least one letter

If the contact already exists, the provided fields are added to it (phones and emails accumulate; birthday and address replace the existing value with an error if already set — use `change_contact` to update them).

---

#### `change_contact`

Updates one or more fields of an existing contact.

```
change_contact name="John Doe" new_name="John Smith"
change_contact name="John Doe" old_phone="+380991234567" new_phone="+380501112233"
change_contact name="John Doe" old_email="john@old.com" new_email="john@new.com"
change_contact name="John Doe" old_birthday="25.12.1990" new_birthday="01.01.1991"
change_contact name="John Doe" old_address="Baker Street 221B" new_address="Main St 1"
```

- **`name`** — required; identifies the contact to update
- To change a phone, email, birthday, or address, both the `old_*` and `new_*` fields must be provided together.

---

#### `remove_contact`

Removes an entire contact or specific fields from it.

```
# Remove the entire contact
remove_contact name="John Doe"

# Remove only a specific phone
remove_contact name="John Doe" phone="+380991234567"

# Remove email, birthday, or address
remove_contact name="John Doe" email="john@example.com"
remove_contact name="John Doe" birthday="yes"
remove_contact name="John Doe" address="yes"
```

- **`name`** — required
- When only `name` is given, the whole contact is deleted.

---

#### `search_contact`

Searches contacts by one or more fields (results must match all provided filters).

```
search_contact name="John"
search_contact phone="+38099"
search_contact email="gmail"
search_contact birthday="25.12"
search_contact address="Baker"
```

- Search is case-insensitive (e.g. "john", "John", "JOHN" are equivalent)

---

#### `show_all_contacts`

Displays every contact in the address book.

```
show_all_contacts
```

---

#### `show_upcoming_birthdays`

Lists contacts with birthdays in the next N days (default: 7). If a birthday falls on a weekend, the congratulation date shifts to the following Monday.

```
show_upcoming_birthdays
show_upcoming_birthdays days="30"
```

---

### Notes Commands

#### `add_note`

Creates a new note or adds content to an existing one.

```
# Create a note with just a title
add_note title="Shopping list"

# Create a note with description and tag
add_note title="Shopping list" description="Buy milk and eggs" tag="#grocery"

# Add a description or tag to an existing note
add_note title="Shopping list" description="Also buy bread"
```

- **`title`** — required; serves as the unique identifier (max 50 characters)
- **`description`** — optional note body (max 100 characters)
- **`tag`** — optional hashtag, must start with `#` (e.g., `#work`, `#personal`)

---

#### `change_note`

Edits the title, description, or tag of an existing note.

```
change_note title="Shopping list" new_title="Weekly groceries"
change_note title="Shopping list" description="Buy milk" new_description="Buy oat milk"
change_note title="Shopping list" tag="#grocery" new_tag="#food"
```

- **`title`** — required; identifies the note
- To change a description or tag, both the old and new values must be provided.

---

#### `remove_note`

Removes an entire note or specific content from it.

```
# Remove the entire note
remove_note title="Shopping list"

# Remove only a description or tag
remove_note title="Shopping list" description="Buy milk"
remove_note title="Shopping list" tag="#grocery"
```

---

#### `search_note`

Searches notes by title substring or tag.

```
search_note title="shop"
search_note tag="#grocery"
```

- Search is case-insensitive across title, tags, and descriptions

---

#### `show_all_notes`

Displays all saved notes.

```
show_all_notes
```

---

### General Commands

| Command           | Description                           |
| ----------------- | ------------------------------------- |
| `options`         | Show the full command reference table |
| `exit` or `close` | Save data and quit the program        |

---

## Data Persistence

On `exit` or `close`, the assistant serializes its full state (address book + notes) to `personal_assistant.pkl` using Python's `pickle` module. On the next launch, this file is automatically loaded. If the file is missing, a fresh assistant starts with no data.

> **Tip:** Back up `personal_assistant.pkl` to preserve your data.

---

## Project Structure

```
goit-personal-assistant/
├── main.py                          # Entry point
├── requirements.txt
├── pyproject.toml                   # CLI configuration (entry point: assistant)
├── personal_assistant.pkl           # Auto-generated save file (after first exit)
└── personal_assistant/
    ├── personal_assistant.py        # PersonalAssistant class, CLI loop, persistence
    ├── address_book/
    │   ├── address_book.py          # AddressBook storage (UserDict subclass)
    │   ├── address_book_event_handlers.py  # Command handler functions
    │   ├── record/
    │   │   ├── record.py            # Record class (single contact)
    │   │   └── record_fields.py     # Field types: Name, Phone, Email, Birthday, Address
    │   ├── models/
    │   │   └── address_book_events.py  # AddressBookEvents enum
    │   └── constants/
    │       └── events_description.py   # Command descriptions and search filters
    ├── notes/
    │   ├── notes.py                 # Notes storage (UserList subclass)
    │   ├── notes_event_handlers.py  # Command handler functions
    │   ├── note/
    │   │   ├── note.py              # Note class
    │   │   └── note_fields.py       # Field types: Title, Description, Tag
    │   ├── models/
    │   │   └── notes_events.py      # NotesEvents enum
    │   └── constants/
    │       └── events_description.py   # Command descriptions
    └── shared/
        ├── error_handler/
        │   ├── decorators/error_handler.py  # @catch_error decorator
        │   └── models/errors.py             # Custom exception classes
        ├── input_handler/
        │   └── decorators/check_input.py    # @check_input decorator
        ├── models/
        │   ├── data_field.py        # Base Field dataclass
        │   └── statuses.py          # Status enum (SUCCESS / ERROR)
        └── utils/
            └── input_data_helpers.py  # parse_input() function
```

---

## Developer Documentation

### Core Classes

---

#### `PersonalAssistant` — `personal_assistant/personal_assistant.py`

Top-level application class. Owns the `AddressBook` and `Notes` instances, runs the interactive CLI loop, and handles persistence.

**Constructor:** `__init__(self)` — creates empty `AddressBook` and `Notes`.

**Methods:**

| Method                        | Parameters                                          | Returns | Description                                                                                                    |
| ----------------------------- | --------------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------- |
| `run(pa_state_path)`          | `pa_state_path: str` — path to the `.pkl` save file | `None`  | Starts the interactive command loop. Prints the welcome table on entry. Loops until `exit`/`close` is entered. |
| `show_options()`              | —                                                   | `None`  | Renders a `rich` table of all available commands with usage descriptions.                                      |
| `__save_state(pa_state_path)` | `pa_state_path: str`                                | `None`  | Calls `save_data()` and prints a success or error message.                                                     |
| `__getstate__()`              | —                                                   | `dict`  | Returns `{"notes": ..., "book": ...}` for `pickle` serialization.                                              |
| `__setstate__(state)`         | `state: dict`                                       | `None`  | Restores `book` and `notes` from the deserialized state dict.                                                  |

**Module-level functions:**

| Function                                  | Parameters                                           | Returns             | Description                                                                                          |
| ----------------------------------------- | ---------------------------------------------------- | ------------------- | ---------------------------------------------------------------------------------------------------- |
| `save_data(personal_assistant, path)`     | `personal_assistant: PersonalAssistant`, `path: str` | `Status`            | Serializes the assistant to disk with `pickle`. Returns `Status.SUCCESS` or `Status.ERROR`.          |
| `start_personal_assistant(pa_state_path)` | `pa_state_path: str` (default: project root `.pkl`)  | `PersonalAssistant` | Loads existing state or creates a new assistant, then calls `run()`. This is the public entry point. |

---

#### `AddressBook` — `personal_assistant/address_book/address_book.py`

Extends `collections.UserDict`. Keys are contact name strings; values are `Record` objects.

| Method                                   | Parameters                       | Returns          | Description                                                                                                                                      |
| ---------------------------------------- | -------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `add_record(record)`                     | `record: Record`                 | `None`           | Adds a record. Raises `AddressBookError` if a contact with the same name already exists.                                                         |
| `rename_record(old_name, new_name)`      | `old_name: str`, `new_name: str` | `None`           | Moves the record to a new key without validation (caller must validate first).                                                                   |
| `find(name)`                             | `name: str`                      | `Record \| None` | Returns the record by name, or `None` if not found.                                                                                              |
| `delete(name)`                           | `name: str`                      | `None`           | Removes a record. Raises `AddressBookError` if not found.                                                                                        |
| `get_upcoming_birthdays(requested_days)` | `requested_days: int`            | `list[dict]`     | Returns a list of `{"name": str, "congratulation_date": str}` for contacts with birthdays in the next N days. Weekend birthdays shift to Monday. |
| `phone_exists(phone)`                    | `phone: str`                     | `bool`           | Returns `True` if the phone number exists in any contact.                                                                                        |
| `email_exists(email)`                    | `email: str`                     | `bool`           | Returns `True` if the email exists in any contact.                                                                                               |

---

#### `Record` — `personal_assistant/address_book/record/record.py`

Stores data for a single contact: name, list of phones, list of emails, optional birthday, optional address.

**Constructor:** `__init__(self, name: str)` — creates a `Name` field; initializes empty `phones` and `emails` lists, `birthday = None`, `address = None`.

| Method                               | Parameters             | Returns         | Description                                                               |
| ------------------------------------ | ---------------------- | --------------- | ------------------------------------------------------------------------- |
| `change_name(new_name)`              | `new_name: str`        | `None`          | Replaces the `Name` field.                                                |
| `validate_name_change(new_name)`     | `new_name: str`        | `None`          | Raises `AddressBookError` if names are identical.                         |
| `add_phone(value)`                   | `value: str`           | `None`          | Appends a `Phone`. Raises if already present on this contact.             |
| `validate_phone_change(old, new)`    | `old: str`, `new: str` | `None`          | Raises if old not found, or old == new, or new already present.           |
| `change_phone(old, new)`             | `old: str`, `new: str` | `None`          | Replaces the matching phone in-place.                                     |
| `remove_phone(value)`                | `value: str`           | `None`          | Removes the matching phone.                                               |
| `find_phone(value)`                  | `value: str`           | `Phone`         | Returns the matching `Phone` or raises `AddressBookError`.                |
| `add_email(value)`                   | `value: str`           | `None`          | Appends an `Email`. Raises if already present.                            |
| `validate_email_change(old, new)`    | `old: str`, `new: str` | `None`          | Raises if old not found, or old == new, or new already present.           |
| `change_email(old, new)`             | `old: str`, `new: str` | `None`          | Replaces the matching email in-place.                                     |
| `remove_email(value)`                | `value: str`           | `None`          | Removes the matching email.                                               |
| `find_email(value)`                  | `value: str`           | `Email \| None` | Returns the matching `Email` or raises `AddressBookError`.                |
| `add_birthday(birthday)`             | `birthday: str`        | `None`          | Sets birthday from a `DD.MM.YYYY` string. Raises if birthday already set. |
| `validate_birthday_change(old, new)` | `old: str`, `new: str` | `None`          | Validates that birthday exists, old matches, and old ≠ new.               |
| `change_birthday(value)`             | `value: str`           | `None`          | Overwrites the birthday.                                                  |
| `add_address(value)`                 | `value: str`           | `None`          | Sets address. Raises if address already set.                              |
| `validate_address_change(old, new)`  | `old: str`, `new: str` | `None`          | Validates that address exists, old matches, and old ≠ new.                |
| `change_address(value)`              | `value: str`           | `None`          | Overwrites the address.                                                   |
| `detailed_view()`                    | —                      | `str`           | Returns a multi-line rich-formatted string showing all fields.            |
| `__str__()`                          | —                      | `str`           | Returns a single-line rich-formatted summary.                             |

---

#### Field Types — `personal_assistant/address_book/record/record_fields.py`

All extend the base `Field` dataclass. Each validates its value in `__init__` and raises `AddressBookError` on failure.

| Class      | Validation rule                                                                                               |
| ---------- | ------------------------------------------------------------------------------------------------------------- |
| `Name`     | Must contain at least one letter (Latin or Cyrillic).                                                         |
| `Phone`    | Must match `+380XXXXXXXXX` (Ukrainian mobile format).                                                         |
| `Birthday` | Must parse as `DD.MM.YYYY`. Stores `.date` as a `datetime` object. Class constant `DATE_FORMAT = "%d.%m.%Y"`. |
| `Email`    | Must match standard email regex `^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$`.                           |
| `Address`  | Must contain at least one letter.                                                                             |

---

#### `Notes` — `personal_assistant/notes/notes.py`

Extends `collections.UserList`. Each element is a `Note` object.

| Method                                               | Parameters              | Returns        | Description                                                                                                                     |
| ---------------------------------------------------- | ----------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `add_note(new_note)`                                 | `new_note: Note`        | `None`         | Appends the note. Raises `NotesError` if a note with the same title already exists.                                             |
| `delete_note(note_title)`                            | `note_title: str`       | `None`         | Removes note by title. Raises `NotesError` if not found.                                                                        |
| `get_note_by_title(note_title)`                      | `note_title: str`       | `Note \| None` | Returns the note or `None` if not found.                                                                                        |
| `find_notes(note_title, note_description, note_tag)` | all `str`, all optional | `list[Note]`   | Returns matching notes. Checks title substring first, then description, then tag. Only the first non-empty argument is applied. |

---

#### `Note` — `personal_assistant/notes/note/note.py`

Stores a single note: a `Title`, a list of `Description` objects, and a list of `Tag` objects.

**Constructor:** `__init__(self, title, descriptions=[], tags=[])` — creates field objects from raw strings.

| Method                            | Parameters             | Returns  | Description                                                            |
| --------------------------------- | ---------------------- | -------- | ---------------------------------------------------------------------- |
| `add_description(text)`           | `text: str`            | `None`   | Appends a description. Raises if it already exists.                    |
| `edit_title(text)`                | `text: str`            | `None`   | Replaces the title. Raises if identical.                               |
| `edit_description(old, new)`      | `old: str`, `new: str` | `None`   | Replaces a description. Raises if new already exists or old not found. |
| `remove_description(description)` | `description: str`     | `None`   | Removes by exact value. Raises if not found.                           |
| `find_descriptions(search_term)`  | `search_term: str`     | `filter` | Returns descriptions matching a regex pattern.                         |
| `add_tag(text)`                   | `text: str`            | `None`   | Appends a tag. Raises if it already exists.                            |
| `edit_tag(old, new)`              | `old: str`, `new: str` | `None`   | Replaces a tag. Raises if new already exists or old not found.         |
| `remove_tag(tag)`                 | `tag: str`             | `None`   | Removes by exact value. Raises if not found.                           |
| `find_tags(search_term)`          | `search_term: str`     | `filter` | Returns tags matching a regex pattern.                                 |

---

#### Note Field Types — `personal_assistant/notes/note/note_fields.py`

All extend `Field` and delegate to `NoteFieldValidation.validate()`.

| Class         | Max length | Pattern requirement                  |
| ------------- | ---------- | ------------------------------------ |
| `Title`       | 50 chars   | At least one alphabetical character  |
| `Description` | 100 chars  | At least one alphabetical character  |
| `Tag`         | 30 chars   | Must match `^#\w+` (starts with `#`) |

**`NoteFieldValidation.validate(value, required_message, range_message, pattern_message, max_text_length, pattern)`** — static validation helper. Checks required (non-empty), length range, and regex pattern. Raises `NotesError` with the appropriate message on failure.

---

### Shared Utilities

#### `parse_input` — `personal_assistant/shared/utils/input_data_helpers.py`

```python
def parse_input(user_input: str) -> tuple[str, dict]
```

Parses a raw CLI input string into a command name and a dict of keyword arguments.

- **Input:** `'add_contact name="John" phone="+380991234567"'`
- **Returns:** `('add_contact', {'name': 'John', 'phone': '+380991234567'})`
- Keys are lowercased. Values have surrounding quotes stripped.
- Arguments must use `key="value"` or `key='value'` syntax.

---

#### `@catch_error` — `personal_assistant/shared/error_handler/decorators/error_handler.py`

Decorator that wraps a handler function in a try/except. Catches `AddressBookError`, `NotesError`, `InputError`, `KeyError`, `IndexError`, `ValueError`, `FileNotFoundError`, and generic `Exception`. Returns a red-colored error string instead of raising, so the CLI loop stays alive on any error.

---

#### `@check_input` — `personal_assistant/shared/input_handler/decorators/check_input.py`

```python
def check_input(*required_args, min_args=None, max_args=None) -> Callable
```

Decorator factory that validates the number of arguments passed to a handler.

- **Strict mode** (positional args given): requires exactly `len(required_args)` arguments.
- **Range mode** (`min_args`/`max_args`): requires between `min_args` and `max_args` arguments (both optional).
- Raises `InputError` with a helpful tip message on failure.

---

#### Custom Exceptions — `personal_assistant/shared/error_handler/models/errors.py`

| Exception                   | Prefix in message      | Use case                                                           |
| --------------------------- | ---------------------- | ------------------------------------------------------------------ |
| `AddressBookError(message)` | `[Address Book Error]` | Business logic violations in contacts (duplicate, not found, etc.) |
| `NotesError(message)`       | `[Notes Error]`        | Business logic violations in notes                                 |
| `InputError(message)`       | `[Input Error]`        | Wrong argument count or missing required fields                    |

---

#### `Field` — `personal_assistant/shared/models/data_field.py`

```python
@dataclass
class Field:
    value: str
    def __str__(self) -> str: ...
```

Base dataclass for all field types. Stores a single `value: str`. `__str__` returns the value.

---

#### `Status` — `personal_assistant/shared/models/statuses.py`

```python
class Status(Enum):
    SUCCESS = auto()
    ERROR = auto()
```

Used by `save_data()` to signal success or failure of file write operations.
