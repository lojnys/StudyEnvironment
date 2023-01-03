from Task import Task

class Tasks():

    """Represents a list of tasks"""

    # EFFECTS: constructs an empty list of tasks
    def __init__(self) -> None:
        self.tasks = []

    # EFFECTS: returns the list of tasks itself
    def getTasks(self) -> list: 
        return self.tasks

    # EFFECTS: adds the given task to the list of tasks
    def addTask(self, task: Task) -> None:
        self.tasks.append(task)

    # EFFECTS: removes the given task from the list of tasks
    def removeTask(self, task: Task) -> None: 
        self.tasks.remove(task)

    # EFFECTS: list in order
    def refresh(self) -> None: 
        self.tasks.sort(key=lambda x: x.getPrio())


    def toJson(self) -> list:
        list = []
        for task in self.tasks:
            list.append(task.toJson())

        return list