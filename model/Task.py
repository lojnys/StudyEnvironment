import string
import sys
from TaskComponent import TaskComponent

sys.path.append("/Users/yushinnam/Desktop/python3/StudyEnvironment/exceptions")

from EmptyStringException import EmptyStringException
from PriorityLessThanOneException import PriorityLessThanOneException


class Task(TaskComponent):

    """Represents a task"""

    # EFFECTS: constructs a task with given description and prio
    def __init__(self, description: str, prio: int=1) -> None:
        super().__init__(description, prio)
        self.finished = False

    # EFFECTS: returns whether the task is finished or not
    def getFinished(self) -> bool:
        return self.finished

    # EFFECTS: sets priority to its given integer
    #          throws PriorityLessThanOneException if given prio is less than 1
    # MODIFIES: self
    def setPrio(self, prio: int) -> None: 
        if (prio < 1):
            raise PriorityLessThanOneException("Priority less than 1 given")
        else: 
            self.prio = prio

    # EFFECTS: sets description as given description
    #          throws EmptyStringException if description does not include a single letter
    # MODIFIES: self
    def setDescription(self, description: str) -> None:
        if (string.ascii_letters not in description):
            raise EmptyStringException("Empty description given")
        else:
            self.description = description

    # EFFECTS: mark the task as finished
    # MODIFIES: self
    def setFinished(self) -> None:
        self.finished = True


    def toJson(self) -> dict:
        """overriding from TaskComponent class"""
        dict = {
            "description": self.description,
            "priotity": self.prio,
            "finished": self.finished
        }
        
        return dict