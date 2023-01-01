

class Task:

    """Represents a task"""

    # REQUIRES: length of description must be > 0
    # EFFECTS: constructs a task with given description and prio
    #          prio is set up as -1 so that its added to the 
    #          back of the list of tasks, but it can be modified
    # MODIFIES: self
    def __init__(self, description: str, prio: int=-1) -> None:
        self.description = description
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