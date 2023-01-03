
class PriorityLessThanOneException(Exception):

    """Raised when the task prio is strictly less than 1"""

    def __init__(self, message):
        super().__init__(message)