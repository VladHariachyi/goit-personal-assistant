from ....address_book.record import Record

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



