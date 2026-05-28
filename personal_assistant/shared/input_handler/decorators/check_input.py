from typing import Callable
from functools import wraps
from ...error_handler import InputError


def check_input(*required_args, min_args: int = None, max_args: int = None) -> Callable:
    def decorator(callback: Callable) -> Callable:
        @wraps(callback)
        def wrapper(args, book):
            actual_count = len(args)

            # STRICT mode
            if required_args:
                expected_count = len(required_args)
                if actual_count != expected_count:
                    raise InputError(
                        f"Incorrect input: expected {expected_count} arguments, "
                        f"but received {actual_count}.\n\n"
                        f"👉 Tip: use 'options' to see available commands and correct format."
                    )

            # RANGE mode (optional)
            else:
                if min_args is not None and actual_count < min_args:
                    raise InputError(
                        f"Incorrect input: expected at least {min_args} arguments, "
                        f"but received {actual_count}.\n\n"
                        f"👉 Tip: use 'options' to see available commands and correct format."
                    )

                if max_args is not None and actual_count > max_args:
                    raise InputError(
                        f"Incorrect input: expected at most {max_args} arguments, "
                        f"but received {actual_count}.\n\n"
                        f"👉 Tip: use 'options' to see available commands and correct format."
                    )

            return callback(args, book)

        return wrapper
    return decorator