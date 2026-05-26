from typing import Callable


def catch_error(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotFoundError as e:
            return f"[red]Oops.. {str(e)}[/red]"
        except ValidationError as e:
            return f"[red]Oops.. {str(e)}[/red]"
        except ValueExistsError as e:
            return f"[red]Oops.. {str(e)}[/red]"
        except ValueError:
            return f"[red]Oops.. Give me the right format of command please.[/red]"
        except KeyError:
            return f"[red]Oops.. Contact was not found.[/red]"
        except IndexError:
            return f"[red]Oops.. Give me the name please."

    return inner


class ValueExistsError(Exception):
    """Raised when contact already exists."""
    pass


class ValidationError(Exception):
    """Raised when phone format is invalid."""
    pass


class NotFoundError(Exception):
    """Raised when the value is not found."""
    pass