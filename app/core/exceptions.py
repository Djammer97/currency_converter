class UserNotFoundException(KeyError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UserIsExistException(ValueError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PasswordIncorrectException(ValueError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class InvalidCurrencyCode(IndexError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
