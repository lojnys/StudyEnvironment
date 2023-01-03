import string
import sys

sys.path.append("/Users/yushinnam/Desktop/python3/StudyEnvironment/exceptions")

from EmptyStringException import EmptyStringException
from PriorityLessThanOneException import PriorityLessThanOneException


class Task:

    """Represents a task"""

    # EFFECTS: constructs a task with given description and prio
    #          pre-set as 1 but can be modified
    #          throws an EmptyStringException if it does not include a single letter
    # MODIFIES: self
    def __init__(self, description: str, prio: int=1) -> None:

        if not any([x in description for x in string.ascii_letters]):        # first make string.ascii_letters into list and then check if each one of them are in the description then logic with not any()
            raise EmptyStringException("Empty description given")
        else:
            self.description = description

        if (prio < 1):
            raise PriorityLessThanOneException("Forbidden priority given")
        else:
            self.prio = prio


    # EFFECTS: returns task's descripition 
    def getDescription(self) -> str: 
        return self.description

    # EFFECTS: returns task's priority
    def getPrio(self) -> int:
        return self.prio

    # EFFECTS: sets priority to its given integer
    # MODIFIES: self
    def setPrio(self, prio: int) -> None: 
        self.prio = prio

    # EFFECTS: sets description as given description
    #          raise EmptyStringException if description does not include a single letter
    # MODIFIES: self
    def setDescription(self, description: str) -> None:
        if (string.ascii_letters not in description):
            raise EmptyStringException("Empty description given")
        else:
            self.description = description


    def toJson(self) -> dict:
        dict = {
            "description": self.description,
            "priotity": self.prio
        }
        
        return dict