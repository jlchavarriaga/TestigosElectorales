class MissingOption(Exception):
    def __init__(self, option: str) -> None:
        super().__init__(f'Option {option} required.')


class InvalidUser(Exception):
    def __init__(self) -> None:
        super().__init__('User already exists.')
