from Task import Task

class Subject(Task):

    """Represents a study task for a given subject"""
    """This class can be used for keeping track of time left to study"""

    # EFFECTS: constructs a study task with given subject name and a goal time of 2 hours
    #          the goal time can be modified
    def __init__(self, subName: str, goal: float = 2) -> None:
        super().__init__(subName + " Study", 1)
        self.goal = goal

    # EFFECTS: returns the goal time of the study task
    def getGoal(self) -> float:
        return self.goal

    # EFFECTS: sets the goal time as the given value
    # MODIFIES: self
    def setGoal(self, goal: float) -> None:
        self.goal = goal

    # overriding toJson() method from Task
    def toJson(self) -> dict:
        diction = super().toJson()
        diction.update({"goal-time": self.getGoal()})
        return diction