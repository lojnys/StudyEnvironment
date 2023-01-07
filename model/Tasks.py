from Task import Task
from TaskComponent import TaskComponent

class Tasks(TaskComponent):

    """Represents a list of tasks"""

    # EFFECTS: constructs an empty list of tasks
    def __init__(self, description: str, prio: int = 1) -> None:
        super().__init__(description, prio)
        self.tasks = []

    # EFFECTS: returns the list of tasks itself
    def getTasks(self) -> list: 
        return self.tasks


    # EFFECTS: adds the given task to the list of tasks
    def addTask(self, task: TaskComponent) -> None:
        self.tasks.append(task)

    # EFFECTS: removes the given task from the list of tasks
    def removeTask(self, task: TaskComponent) -> None: 
        self.tasks.remove(task)

    # EFFECTS: list in order
    def refresh(self) -> None: 
        self.tasks.sort(key=lambda x: x.getPrio())


    def toJson(self) -> dict:
        """overriding from TaskComponent class"""
        list = []
        for task in self.tasks:
            list.append(task.toJson())

        return {"description": self.description, "list": list}


# tasks = Tasks("School")
# tasks.addTask(Tasks("Work"))
# tasks.addTask(Task("Math 300 Study"))
# tasks.addTask(Tasks("Home"))

# for task in tasks.getTasks():
#     if (task.getDescription() == "Work"):
#         task.addTask(Task("Doing the Laundry"))

# print(tasks.toJson())