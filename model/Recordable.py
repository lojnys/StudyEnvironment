import os
import json

class Recordable():

    """An abstract class that represents a recordable class"""
    
    # EFFECTS: constructs a recordable object and create a csv file
    def __init__(self, name: str) -> None:
        self.filename = "/Users/yushinnam/Desktop/python3/StudyEnvironment/data/" + name + ".json"
        with open(self.filename, 'w') as file:
            pass
    
    # EFFECTS: writes the given input on json file
    def write(self, input) -> None: 
        with open(self.filename, 'w') as file:
            json.dump(input, file)

    # EFFECTS: loads from json file
    def read(self) -> None:
        with open(self.filename, 'r') as file:
            return json.load(file)

    # EFFECTS: removes the file
    def remove(self) -> None:
        os.remove(self.filename)
