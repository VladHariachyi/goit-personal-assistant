from ....address_book.record import Record
from ...error_handler import InputError

def format_record(record: Record) -> str:
    return str(record)


def parse_contact_fields(values: list[str]) -> dict:
    parsed = {}

    for value in values:
        if "=" not in value:
            continue

        key, val = value.split("=", 1)
        parsed[key.strip().lower()] = val.strip()

    return parsed


def validate_change_contact(fields: dict, pairs) -> None:
    for old, new in pairs:
        if old in fields or new in fields:
            if (old in fields) != (new in fields):
                raise InputError(f"Both {old} and {new} must be provided.")

