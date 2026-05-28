from functools import wraps
from typing import Callable

from errors import (
    AddressBookError,
    NotesError,
    InputError
)


def catch_error(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (AddressBookError, NotesError, InputError) as error:
            print(f"[red]{error}[/red]")
        except KeyError as missed_key:
            print(f"[red][Missed Key Error] '{missed_key}' doest not exist[/red]")
            return None
        except IndexError:
            print(f"[red][Index error] The requested index is out of the range[/red]")
            return None
        except ValueError:
            print(f"[red][Value error] Can't process the operation due to incorrect input[/red]")
            return None
        except FileNotFoundError as e:
            print(e)
            return None
        except Exception as error:
            print(f"[red][Error] The system can't respond: {error}[/red]")

    return wrapper