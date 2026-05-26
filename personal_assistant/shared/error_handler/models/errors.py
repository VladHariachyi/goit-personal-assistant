class UserInputError(Exception):
    def __init__(self, message: str):
        super().__init__(f"[Input error] {message}")