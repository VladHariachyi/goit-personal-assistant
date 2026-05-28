from typing import Callable
from functools import wraps
from ...error_handler.models.errors import UserInputError


def check_input(*required_args) -> Callable:
    def decorator(callback: Callable) -> Callable:
        @wraps(callback)
        def wrapper(args, book):
            expected_count = len(required_args)
            actual_count = len(args)

            if actual_count != expected_count:
                func_name = callback.__name__

                if expected_count == 0:
                    error_msg = (
                        f"Команда '{func_name}' не приймає параметрів. "
                        f"Передано: {actual_count}, очікується: 0"
                    )
                elif expected_count == 1:
                    error_msg = (
                        f"Команда '{func_name}' очікує 1 параметр: {required_args[0]}. "
                        f"Передано: {actual_count}, очікується: {expected_count}"
                    )
                else:
                    params_str = ", ".join(required_args)
                    error_msg = (
                        f"Команда '{func_name}' очікує {expected_count} параметрів: {params_str}. "
                        f"Передано: {actual_count}, очікується: {expected_count}"
                    )

                raise UserInputError(error_msg)

            return callback(args, book)

        return wrapper
    return decorator