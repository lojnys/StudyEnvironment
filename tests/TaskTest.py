import unittest
import sys

sys.path.append("/Users/yushinnam/Desktop/python3/StudyEnvironment/exceptions")
from EmptyStringException import EmptyStringException
from PriorityLessThanOneException import PriorityLessThanOneException

sys.path.append("/Users/yushinnam/Desktop/python3/StudyEnvironment/model")
from Task import Task

class TaskTest(unittest.TestCase):

    def test_initPass(self):

        try:
            testTask = Task("Get ready to go out")
        
        except EmptyStringException:
            print("Unexpected EmptyStringException raised")
            raise False
        except PriorityLessThanOneException:
            print("Unexpected PriorityLessThanOneException raised")
            raise False

        self.assertEqual(testTask.getDescription(), "Get ready to go out")
        self.assertEqual(testTask.getPrio(), 1)

    
    def test_initEmptyStringExceptionRaised(self):

        try:
            testTask1 = Task("")
            raise False

        except EmptyStringException:
            pass

        except PriorityLessThanOneException as pltoe:
            raise pltoe("Unexpected PriorityLessThanOneException raised")

    def test_initPriorityLessThanOneExceptionRaised(self):

        try:
            testTask2 = Task("a", 0)
            raise False

        except EmptyStringException as ese:
            raise ese("Unexpected EmptyStringException raised")

        except PriorityLessThanOneException:
            pass
    

    def test_toJson(self):
        task = Task("abcd", 2)

        self.assertEqual(task.toJson(), {"description": "abcd", "priority": 2, "finished": False})


if __name__ == "__main__":
    unittest.main()
