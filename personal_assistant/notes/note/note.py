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
        formatted_description = self.__format_list_text_entity(self.__get_descriptions_text())
        formatted_tags = self.__format_list_text_entity(self.__get_tags_text())

        desctription_text = (
            f"[cyan]{'\n'.join(formatted_description)}[/cyan]" 
            if len(formatted_description) 
            else "[yellow3]• Empty[/yellow3]"
        )
        tags_text = (
            f"[cyan]{'\n'.join(formatted_tags)}[/cyan]" 
            if len(formatted_tags) 
            else "[yellow3]• Empty[/yellow3]"
        )

        return (
            f"[green]Title: [/green][cyan]{self.title}[/cyan]"
            f"\n[green]Descriptions:[/green]\n"
            f"{desctription_text}"
            f"\n[green]Tags:[/green]\n"
            f"{tags_text}"
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
    
    def add_tag(self, text: str) -> None:
        is_exist = text in self.__get_tags_text()

        if is_exist:
            raise NotesError("The tag is already exist")

        tag = Tag(text)
        self.tags.append(tag)

    def edit_tag(self, old_tag: str, new_tag: str) -> None:
        is_exist = new_tag in self.__get_tags_text()

        if is_exist:
            raise NotesError("The tag is already exists")
        
        found_tag_index = self.__get_tag_index(old_tag)
        
        self.tags[found_tag_index] = Tag(new_tag)

    def remove_tag(self, tag: str) -> None:
        found_tag_index = self.__get_tag_index(tag)

        self.tags.pop(found_tag_index)

    def find_tags(self, search_term: str) -> list[Tag] | None:
        return self.__find_by_text_value(search_term, self.tags)

    def __find_by_text_value(self, search_term: str, data: list[Field]) -> list | None:
        pattern = re.escape(search_term)

        return list(filter(lambda item: re.search(pattern, item.value), data))
    
    def __get_descriptions_text(self) -> list[str]:
        return [d.value for d in self.descriptions]
    
    def __get_tags_text(self) -> list[str]:
        return [t.value for t in self.tags]
    
    def __get_description_index(self, description: str) -> int | None:
        found_description_index = None

        try:
           found_description_index = [d.value for d in self.descriptions].index(description) 
        except:
            raise NotesError(f"The description is not found: '{description}'")
        
        return found_description_index
    
    def __get_tag_index(self, tag: str) -> int | None:
        found_tag_index = None

        try:
           found_tag_index = [t.value for t in self.tags].index(tag) 
        except:
            raise NotesError(f"The tag is not found: '{tag}'")
        
        return found_tag_index
    
    def __format_list_text_entity(self, list: list[str]) -> list[str]:
        return [f"• {item}" for item in list]
