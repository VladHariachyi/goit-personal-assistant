class Note:

    def __init__(
        self,
        text,
        tags=None
    ):

        self.text = text

        self.tags = tags or []  # Якщо tags не передали створюється пустий список.

    def add_tag(self, tag):

        tag = tag.lower()

        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag):

        tag = tag.lower()

        if tag in self.tags:
            self.tags.remove(tag)

    def has_tag(self, tag):

        return tag.lower() in self.tags

    def __str__(self):

        tags = ", ".join(self.tags)

        return (
            f"Note: {self.text}\n"
            f"Tags: {tags}"
        )