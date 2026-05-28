from typing import Callable
from functools import wraps
from ..models import (
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
            return(f"[red]{error}[/red]")
        except KeyError as missed_key:
            return(f"[red][Missed Key Error] '{missed_key}' does not exist[/red]")
        except IndexError:
            # print('Please use the correct format of the command')
            return(f"[red][Index error] The requested index is out of the range[/red]")
        except ValueError:
            return(f"[red][Value error] Can't process the operation due to incorrect input[/red]")
        except FileNotFoundError as e:
            return(e)
        except Exception as error:
            return(f"[red][Error] The system can't respond: {error}[/red]")

    return wrapper
