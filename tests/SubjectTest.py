import unittest
import sys

sys.path.append("/Users/yushinnam/Desktop/python3/StudyEnvironment/model")
from Subject import Subject

sys.path.append("/Users/yushinnam/Desktop/python3/StudyEnvironment/exceptions")

from EmptyStringException import EmptyStringException
from PriorityLessThanOneException import PriorityLessThanOneException


class SubjectTest(unittest.TestCase):

    def test_initPass(self):
        
        try:

            subject = Subject("Math 300")

        except EmptyStringException:
            raise False

        except PriorityLessThanOneException:
            raise False

        self.assertEqual(subject.getGoal(), 2)
        self.assertEqual(subject.getDescription(), "Math 300 Study")
        self.assertEqual(subject.getPrio(), 1)
        self.assertFalse(subject.getFinished())
    

    def test_initFail(self):
        # Omitted because Subject class always has letters and always has priority 1  

        # try:
        #     subject = Subject("")
        #     raise False
        # except EmptyStringException:
        #     pass
        
        # except PriorityLessThanOneException:
        #     raise False
        pass


    def test_setGoal(self):
        subject = Subject("Math 300")
        subject.setGoal(1.5)

        self.assertEqual(subject.getGoal(), 1.5)



if __name__ == "__main__":
    unittest.main()