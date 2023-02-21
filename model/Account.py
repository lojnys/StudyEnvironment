

from Recordable import Recordable
from Tasks import Tasks
from Task import Task
import sys
import string
sys.path.append("/Users/yushinnam/Desktop/python3/StudyEnvironment/exceptions")

from EmptyStringException import EmptyStringException 

class Account(): 

    """Represents an account"""

    # EFFECTS: constructs an account with give username, password, email, and with no tasks
    #          raise EmptyStringException if either username or password does not include 
    #          a single character. 
    def __init__(self, username: str, password: str, tasks: list = []) -> None:
        if not any([x in username or x in password for x in string.ascii_letters]):
            raise EmptyStringException("Empty username or password given")
        else:
            self.username = username
            self.password = password
            self.tasks = Tasks(tasks)
            self.logInStatus = False

    # EFFECTS: delets the object
    def __del__(self):
        pass


    # EFFECTS: returns username
    def getUsername(self) -> str:
        return self.username

    # EFFECTS: returns password
    def getPassword(self) -> str:
        return self.password

    # EFFECTS: returns tasks
    def getTasks(self) -> Tasks:
        return self.tasks

    # EFFECTS: returns log in status
    def getLogInStatus(self) -> bool:
        return self.logInStatus
    

    # EFFECTS: sets username with given input
    # MODIFIES: self
    def setUsername(self, username: str) -> None:
        self.username = username
    
    # EFFECTS: sets password with given input
    # MODIFIES: self
    def setPassword(self, password: str) -> None:
        self.password = password






    # EFFECTS: sets log in status to True
    # MODIFIES: self    
    def logIn(self) -> None:
        self.logInStatus = True

    #? EFFECTS: sets log in status to False
    #: MODIFIES self
    def logOut(self) -> None:
        self.logInStatus = False

    # EFFECTS: saves the contents to csv file
    def toJson(self) -> dict:
        input = {
            "username": self.username,
            "password": self.password,
            "tasks": self.tasks.toJson(),
            "log-in": self.logInStatus
        }

        return input