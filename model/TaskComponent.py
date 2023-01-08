from abc import ABCMeta, abstractmethod
import string
import sys
sys.path.append("/Users/yushinnam/Desktop/python3/StudyEnvironment/exceptions")
from EmptyStringException import EmptyStringException
from PriorityLessThanOneException import PriorityLessThanOneException


class TaskComponent(metaclass=ABCMeta):

    """Represents a task component"""
    """TaskComponent, Task, Tasks classes construct a Composite Design Pattern"""
    
    # EFFECTS: contructs a task component, either a task (leaf) or a tasks (composite)
    #          throws an EmptyStringException if description does not include a sinlge letter
    #          throws a PriorityLessThanOneException if prioriry is less than 1
    def __init__(self, description: str, prio: int=1) -> None:

        if not any([x in description for x in string.ascii_letters]):        # first make string.ascii_letters into list and then check if each one of them are in the description then logic with not any()
            raise EmptyStringException("Empty description given")
        else:
            self.description = description

        if (prio < 1):
            raise PriorityLessThanOneException("Forbidden priority given")
        else:
            self.prio = prio

    # EFFECTS: returns description
    def getDescription(self) -> str:
        return self.description

    # EFFECTS: returns priority
    def getPrio(self) -> int:
        return self.prio


    @abstractmethod
    def toJson(self) -> None:
        """implement in child class"""
