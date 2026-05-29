import re

from ...shared.models import Field
from ...shared.error_handler import NotesError


class NoteFieldValidation():
    max_range_text_placeholder = "[max_text_range]"

    @staticmethod
    def validate(
        value: str, 
        required_message: str = "",
        range_message: str = "",
        pattern_message: str = "",
        max_text_lenght: int = 50,
        pattern = r"[a-z]+",
    ) -> None:
        if required_message and not value.strip():
            raise NotesError(required_message)
        
        if range_message and len(value) > max_text_lenght:
            updated_message = range_message.replace(
                NoteFieldValidation.max_range_text_placeholder,
                f"'{max_text_lenght}'"
            )

            raise NotesError(updated_message)

        if pattern_message:
            is_valid_by_pattern = re.search(pattern, value, re.IGNORECASE)

            if (not is_valid_by_pattern):
                    raise NotesError(pattern_message)


class Title(Field):
    """Note title field"""
    def __init__(self, text: str) -> None:
        NoteFieldValidation.validate(
            value = text,
            required_message = "The note title is required",
            range_message = (
                "The note title is too big, the max allowed characters" 
                f"is {NoteFieldValidation.max_range_text_placeholder}"
            ),
            pattern_message = "The note title should consists at least one alphabetical character"
        )
        super().__init__(text)
        
        
class Description(Field):
    """Note description field"""
    def __init__(self, text: str) -> None:
        NoteFieldValidation.validate(
            value = text,
            required_message = "The note description could not be empty",
            range_message = (
                "The note description is too big, the max allowed characters" 
                f"is {NoteFieldValidation.max_range_text_placeholder}"
            ),
            pattern_message = "The note description should consists at least one alphabetical character",
            max_text_lenght = 100
        )
        super().__init__(text)


class Tag(Field):
    """Note tag field"""
    def __init__(self, text: str) -> None:
        NoteFieldValidation.validate(
            value = text,
            required_message = "",
            range_message = "",
            pattern_message = "",
            max_text_lenght = 100,
            pattern = ""
        )
        super().__init__(text)