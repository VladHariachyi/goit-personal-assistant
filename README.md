# Personal Assistant CLI

A command-line personal assistant built with Python for managing contacts and notes. Data persists between sessions via binary serialization (`pickle`).

> **Project:** GoIT / Neoversity — Python Programming  
> **Prefix:** `PA` (used in all branch names and commit messages)

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Commands Reference](#commands-reference)
- [Developer Documentation](#developer-documentation)
- [Contributing](#contributing)

---

## Features

**Contact Management**

- Add contacts with a name and one or more phone numbers
- Change or remove phone numbers
- Add and display birthdays
- List all contacts
- Show contacts with upcoming birthdays (within the next 7 days, weekend-adjusted)
- Data is saved to `addressbook.pkl` on exit and restored on startup

**Notes** _(in development)_

- Architecture scaffolded — `Notes` and `Note` classes are ready for implementation

---

## Project Structure

```
goit-personal-assistant/
├── main.py                                          # Entry point
├── addressbook.pkl                                  # Serialized data (auto-created)
├── requirements.txt
├── CONTRIBUTION.md
│
└── personal_assistant/
    ├── __init__.py
    ├── personal_assistant.py                        # PersonalAssistant class — main CLI loop
    │
    ├── address_book/
    │   ├── __init__.py
    │   ├── address_book.py                          # AddressBook class (UserDict)
    │   └── record/
    │       ├── __init__.py
    │       ├── record.py                            # Record class
    │       └── record_fields.py                     # Field, Name, Phone, Birthday
    │
    ├── notes/
    │   ├── __init__.py
    │   ├── notes.py                                 # Notes class (stub)
    │   └── note/
    │       ├── __init__.py
    │       └── note.py                              # Note class (stub)
    │
    └── shared/
        ├── __init__.py
        ├── error_handler/
        │   ├── decorators/
        │   │   └── catch_error.py                   # @catch_error decorator + custom exceptions
        │   └── models/
        │       └── errors.py                        # UserInputError
        ├── event_handler/
        │   ├── event_handler.py                     # handle_event() dispatcher
        │   ├── models/
        │   │   ├── address_book_events.py           # AddressBookEvents enum
        │   │   └── notes_events.py                  # NotesEvents enum
        │   └── utils/
        │       ├── address_book_event_handlers.py   # All address book command handlers
        │       ├── notes_event_handlers.py          # Notes handlers (stub)
        │       └── check_event_context.py           # is_address_book_event / is_notes_event
        └── input_handler/
            └── decorators/
                └── check_input.py                   # check_input decorator (stub)
```

---

## Installation

**Prerequisites:** Python 3.10+

```bash
# 1. Clone the repository
git clone https://github.com/VladHariachyi/goit-personal-assistant.git
cd goit-personal-assistant

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate       # Linux / macOS
venv\Scripts\activate          # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Usage

```bash
python main.py
```

You will see:

```
Welcome to the assistant bot!
Enter a command:
```

Type a command and press **Enter**. Use `exit` or `close` to save and quit.

---

## Commands Reference

| Command          | Arguments                        | Description                                         |
| ---------------- | -------------------------------- | --------------------------------------------------- |
| `hello`          | —                                | Greet the assistant                                 |
| `add`            | `<name> <phone>`                 | Add a new contact or add a phone to an existing one |
| `change`         | `<name> <old_phone> <new_phone>` | Replace a phone number for a contact                |
| `phone`          | `<name>`                         | Show all phone numbers for a contact                |
| `all`            | —                                | List all saved contacts                             |
| `add-birthday`   | `<name> <DD.MM.YYYY>`            | Set a birthday for a contact                        |
| `show-birthday`  | `<name>`                         | Show a contact's birthday                           |
| `birthdays`      | —                                | Show contacts with birthdays in the next 7 days     |
| `exit` / `close` | —                                | Save data and exit                                  |

---

## Developer Documentation

### `main.py`

Minimal entry point. Creates a `PersonalAssistant` instance and calls `run()`.

```python
def main() -> None:
    app = PersonalAssistant()
    app.run()
```

---

### `PersonalAssistant`

**File:** `personal_assistant/personal_assistant.py`

The main application class. Initialises data stores and runs the CLI event loop.

**`__init__(self)`**

- Calls `load_data()` to restore the address book from `addressbook.pkl`
- Creates an empty `Notes()` instance

**`run(self) -> None`**

- Prints the welcome message
- Reads user input in an infinite loop
- Routes commands via a `match/case` block
- Calls `save_data(book)` and breaks on `exit` / `close`

---

### `AddressBook`

**File:** `personal_assistant/address_book/address_book.py`  
Inherits from `collections.UserDict`. Stores `Record` objects keyed by contact name.

| Method                   | Parameters       | Returns          | Description                                                                                                                                                      |
| ------------------------ | ---------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `add_record`             | `record: Record` | `None`           | Adds a record; raises `ValueExistsError` if name already exists                                                                                                  |
| `find`                   | `name: str`      | `Record \| None` | Returns the record or `None`                                                                                                                                     |
| `delete`                 | `name: str`      | `None`           | Removes a record; raises `KeyError` if not found                                                                                                                 |
| `get_upcoming_birthdays` | —                | `list[dict]`     | Returns contacts whose birthday falls within the next 7 days. Weekends are shifted to Monday. Each dict has keys `name` and `congratulation_date` (`DD.MM.YYYY`) |
| `phone_exists`           | `phone: str`     | `bool`           | Returns `True` if the phone number already exists in any record                                                                                                  |

---

### `Record`

**File:** `personal_assistant/address_book/record/record.py`  
Stores a single contact's data.

**Attributes:**

- `name` (`Name`) — required
- `phones` (`list[Phone]`) — zero or more phone numbers
- `birthday` (`Birthday | None`) — optional

| Method         | Parameters                           | Returns | Description                                                                                |
| -------------- | ------------------------------------ | ------- | ------------------------------------------------------------------------------------------ |
| `add_phone`    | `value: str`                         | `None`  | Validates and appends a phone; raises `ValueExistsError` if duplicate                      |
| `remove_phone` | `value: str`                         | `None`  | Removes a phone by value                                                                   |
| `edit_phone`   | `old_number: str`, `new_number: str` | `None`  | Replaces a phone; raises `ValueExistsError` if identical, `NotFoundError` if old not found |
| `find_phone`   | `value: str`                         | `Phone` | Returns matching `Phone`; raises `NotFoundError`                                           |
| `add_birthday` | `birthday: str`                      | `None`  | Sets birthday; raises `ValueExistsError` if already set                                    |
| `__str__`      | —                                    | `str`   | Returns a rich-formatted string with name, phones, and birthday                            |

---

### Field Classes

**File:** `personal_assistant/address_book/record/record_fields.py`

All fields inherit from `Field` (a `@dataclass` with a single `value: str` attribute).

| Class      | Validation                     | Format         |
| ---------- | ------------------------------ | -------------- |
| `Name`     | Non-empty string (after strip) | Any string     |
| `Phone`    | Exactly 10 digits              | `"0501234567"` |
| `Birthday` | Parseable date string          | `"DD.MM.YYYY"` |

All validation failures raise `ValidationError`.

---

### Error Handler

**File:** `personal_assistant/shared/error_handler/decorators/catch_error.py`

#### `@catch_error` decorator

Wraps a handler function and maps exceptions to user-friendly `rich`-formatted strings.

| Exception caught   | Message returned                                     |
| ------------------ | ---------------------------------------------------- |
| `NotFoundError`    | `Oops.. <message>` (red)                             |
| `ValidationError`  | `Oops.. <message>` (red)                             |
| `ValueExistsError` | `Oops.. <message>` (red)                             |
| `ValueError`       | `Oops.. Give me the right format of command please.` |
| `KeyError`         | `Oops.. Contact was not found.`                      |
| `IndexError`       | `Oops.. Give me the name please.`                    |

#### Custom Exceptions

| Class              | Raised when                                |
| ------------------ | ------------------------------------------ |
| `ValidationError`  | Field format is invalid (phone, date)      |
| `ValueExistsError` | Duplicate value (contact, phone, birthday) |
| `NotFoundError`    | A record or phone was not found            |
| `UserInputError`   | General user input problem                 |

---

### Address Book Event Handlers

**File:** `personal_assistant/shared/event_handler/utils/address_book_event_handlers.py`

All handlers are decorated with `@catch_error`.

#### `parse_input(user_input: str) -> tuple[str, ...]`

Splits raw user input into a command and arguments.

```python
parse_input("add John 0501234567")
# → ("add", "John", "0501234567")
```

#### `add_contact(args, book) -> str`

Adds a phone to a new or existing contact. Checks for global phone uniqueness before adding.

- `args`: `[name, phone]`
- Returns: `"Contact added."` or `"Contact updated."`

#### `change_contact(args, book) -> str`

Replaces `old_phone` with `new_phone` for the named contact.

- `args`: `[name, old_phone, new_phone]`

#### `show_phone(args, book) -> str`

Returns a comma-separated list of phone numbers for the named contact.

- `args`: `[name]`

#### `show_all(book) -> str`

Returns a newline-separated string of all contacts (via `Record.__str__`).

#### `add_birthday(args, book) -> str`

Adds a birthday to the named contact.

- `args`: `[name, "DD.MM.YYYY"]`

#### `show_birthday(args, book) -> str`

Returns the birthday string for the named contact.

- `args`: `[name]`

#### `birthdays(book) -> str`

Returns upcoming birthday congratulations for the next 7 days. Weekend dates are shifted to Monday.

#### `save_data(book, filename="addressbook.pkl") -> None`

Serializes the `AddressBook` to disk using `pickle`.

#### `load_data(filename="addressbook.pkl") -> AddressBook`

Deserializes the `AddressBook` from disk. Returns a new empty `AddressBook` if the file is not found.

---

### Event Routing

**File:** `personal_assistant/shared/event_handler/utils/check_event_context.py`

#### `is_address_book_event(event: str) -> bool`

Returns `True` if the event string matches a value in the `AddressBookEvents` enum.

#### `is_notes_event(event: str) -> bool`

Returns `True` if the event string matches a value in the `NotesEvents` enum.

---

### Enums

**`AddressBookEvents`** — `personal_assistant/shared/event_handler/models/address_book_events.py`

- `ADD_CONTACT = "add_contact"`

**`NotesEvents`** — `personal_assistant/shared/event_handler/models/notes_events.py`

- `ADD_NOTE = "add_note"`

---

## Contributing

See [CONTRIBUTION.md](./CONTRIBUTION.md) for the full workflow. Summary:

1. Branch from `main` using the pattern: `feat/PA-<number>-<short-description>`
2. Implement your changes
3. Commit with: `feat: <message> [PA-<number>]`
4. Open a Pull Request — direct pushes to `main` are not allowed
5. Merge only after review and approval

**Branch prefix types:** `feat/`, `fix/`, `refactoring/`

---

## Dependencies

```
rich==15.0.0          # Colored terminal output
```

---

## License

MIT
