
class EmptyStringException(Exception):

    """Raised when the string does not include a single alphabet"""

    def __init__(self, message):
        super().__init__(message)