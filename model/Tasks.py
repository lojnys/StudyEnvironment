from Task import Task
import sys
import string
sys.path.append("/Users/yushinnam/Desktop/python3/StudyEnvironment/exceptions")

from EmptyStringException import EmptyStringException
from PriorityLessThanOneException import PriorityLessThanOneException

class Tasks():

    """Represents a list of tasks"""
    #!!!
    # EFFECTS: constructs an empty list of tasks
    def __init__(self, prev: list) -> None:
        if prev == []:
            self.tasks = prev
        else:
            self.tasks =  self.fromJson(prev)


    def fromJson(self, list: list) -> list:
        result = []
        for entry in list:
            task = Task(entry["description"], entry["priority"])
            result.append(task)

        return result

    def toJson(self) -> list:
        list = []
        for task in self.tasks:
            list.append(task.toJson())

        return list


    # EFFECTS: returns the list of tasks itself
    def getTasks(self) -> list: 
        return self.tasks

    def setTasks(self, tasks: list) -> None:
        self.tasks = tasks

    #  # EFFECTS: returns description
    # def getDescription(self) -> str:
    #     return self.description

    # # EFFECTS: returns priority
    # def getPrio(self) -> int:
    #     return self.prio

    # EFFECTS: adds the given task to the list of tasks
    def addTask(self, task: Task) -> None:
        self.tasks.append(task)

    # EFFECTS: removes the given task from the list of tasks
    def removeTask(self, task: Task) -> None: 
        self.tasks.remove(task)

    # EFFECTS: list in order
    def refresh(self) -> None: 
        self.tasks.sort(key=lambda x: x.getPrio())


    # def toJson(self) -> list:
    #     list = []
    #     for entry in self.tasks:
    #         task = Task(entry["description"], entry["priority"])
    #         list.append(task.toJson())

    #     return list


    # def fromJson(self, list: list) -> list:
    #     result = []
    #     for entry in list:
    #         task = Task(entry["description"], entry["priority"])
    #         result.append(task)

    #     return result