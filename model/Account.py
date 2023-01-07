from Recordable import Recordable
from Tasks import Tasks
from Task import Task
import sys
import string
sys.path.append("/Users/yushinnam/Desktop/python3/StudyEnvironment/exceptions")

from EmptyStringException import EmptyStringException 

class Account(Recordable): 

    """Represents an account"""

    # EFFECTS: constructs an account with give username, password, email, and with no tasks
    #          raise EmptyStringException if either username or password does not include 
    #          a single character. 
    def __init__(self, username: str, password: str, email: str) -> None:
        super().__init__(username)
        if not any([x in username or x in password for x in string.ascii_letters]):
            raise EmptyStringException("Empty username or password given")
        else:
            self.username = username
            self.password = password
            self.email = email
            self.tasks = Tasks("Main")
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

    # EFFECTS: returns email
    def getEmail(self) -> str:
        return self.email

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

    # EFFECTS: sets email with given input
    # MODIFIES: self
    def setEmail(self, email: str) -> None:
        self.email = email





    # EFFECTS: sets log in status to True
    # MODIFIES: self    
    def logIn(self) -> None:
        self.logInStatus = True
        self.save()

    # EFFECTS: saves the contents to csv file
    def save(self) -> None:
        input = {
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "tasks": self.tasks.toJson(),
            "log-in": self.logInStatus
        }

        super().write(input)

    # EFFECTS: loads the contents from csv file
    def load(self) -> None:
        return super().read()