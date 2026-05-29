import re

from .note_fields import Title, Description, Tag
from ...shared.models import Field
from ...shared.error_handler import NotesError


class Note:
    def __init__(
        self, 
        title: str, 
        descriptions: list[str] = [], 
        tags: list[str] = []
    ) -> None:
        self.title = Title(title)
        self.descriptions = [Description(d) for d in descriptions] if descriptions else []
        self.tags = [Tag(t) for t in tags] if tags else []

    def __str__(self):
        fomatted_description = self.__format_list_text_entity(self.__get_descriptions_text())
        fomatted_tags = self.__format_list_text_entity(self.__get_tags_text())

        return (
            f"[green]Title: [/green][cyan]{self.title}[/cyan]"
            f"\n[green]Descriptions[/green]\n"
            f"[cyan]{'\n'.join(fomatted_description)}[/cyan]"
            f"\n[green]Tags[/green]\n"
            f"[cyan]{'\n'.join(fomatted_tags)}[/cyan]"
        )

    def add_description(self, text: str) -> None:
        is_exist = text in self.__get_descriptions_text()

        if is_exist:
            raise NotesError("The description is already exist")

        description = Description(text)
        self.descriptions.append(description)

    def edit_title(self, text: str) -> None:
        if self.title == text:
            raise NotesError("The title is already exists")
        
        title = Title(text)
        self.title = title

    def edit_description(self, old_description: str, new_description: str) -> None:
        is_exist = new_description in self.__get_descriptions_text()

        if is_exist:
            raise NotesError("The description is already exists")
        
        found_description_index = self.__get_description_index(old_description)
        
        self.descriptions[found_description_index] = Description(new_description)

    def remove_description(self, description: str) -> None:
        found_description_index = self.__get_description_index(description)

        self.descriptions.pop(found_description_index)

    def find_descriptions(self, search_term: str) -> list[Description] | None:
        return self.__find_by_text_value(search_term, self.descriptions)
    
    def add_tag(self, tag: str) -> None:
        # TODO
        pass

    def edit_tag(self, old_tag: str, new_tag: str) -> None:
        # TODO
        pass

    def remove_tag(self, tag: str) -> None:
        # TODO
        pass

    def find_tags(self, search_term: str) -> list[Tag] | None:
        return self.__find_by_text_value(search_term, self.tags)

    def __find_by_text_value(self, search_term: str, data: list[Field]) -> list | None:
        pattern = rf"{search_term}"

        return filter(lambda item: re.search(pattern, item.value), data)
    
    def __get_descriptions_text(self) -> list[str]:
        return [d.value for d in self.descriptions]
    
    def __get_tags_text(self) -> list[str]:
        return [d.value for d in self.tags]
    
    def __get_description_index(self, description: str) -> int | None:
        found_description_index = None

        try:
           found_description_index = self.descriptions.index(description) 
        except:
            raise NotesError(f"The description is not found: '{description}'")
        
        return found_description_index
    
    def __format_list_text_entity(self, list: list[str]) -> list[str]:
        return [f"- {item}" for item in list]
