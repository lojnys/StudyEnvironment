

class Task:

    """Represents a task"""

    # REQUIRES: length of description must be > 0
    # EFFECTS: constructs a task with given description and prio
    #          pre-set as 1 but can be modified
    #          throws an EmptyStringException if len(description) <= 0
    # MODIFIES: self
    def __init__(self, description: str, prio: int=1) -> None:
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

    # EFFECTS: sets description as given description
    # MODIFIES: self
    def setDescription(self, description: str) -> None:
        self.description = description