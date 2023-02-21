import unittest
import sys

sys.path.append("/Users/yushinnam/Desktop/python3/StudyEnvironment/exceptions")
from EmptyStringException import EmptyStringException
from PriorityLessThanOneException import PriorityLessThanOneException

sys.path.append("/Users/yushinnam/Desktop/python3/StudyEnvironment/model")
from Tasks import Tasks
from Task import Task

class TasksTest(unittest.TestCase):

    @staticmethod
    def count_elem(list: list) -> int:
        """helper function"""

        count = 0
        for element in list:
            count += 1
        return count


    def test_initPass(self):
        
        try:
            tasks = Tasks("School")

        except EmptyStringException:
            raise False
        except PriorityLessThanOneException:
            raise False
        
        self.assertEqual(self.count_elem(tasks.getTasks()), 0)
        self.assertEqual(tasks.getDescription(), "School")
        self.assertEqual(tasks.getPrio(), 1)

    
    def test_initFail(self):

        try: 
            tasks1 = Tasks("")
            raise False

        except EmptyStringException:
            pass

        except PriorityLessThanOneException:
            raise False


        try: 
            tasks2 = Tasks("a", 0)
            raise False

        except EmptyStringException:
            raise False
        
        except PriorityLessThanOneException:
            pass

    

    def test_addOneTask(self):
        tasks = Tasks("School")
        tasks.addTask(Task("Math 300 Homework"))

        self.assertEqual(self.count_elem(tasks.getTasks()), 1)
        self.assertEqual(tasks.getTasks()[0].getDescription(), "Math 300 Homework")
        self.assertEqual(tasks.getTasks()[0].getPrio(), 1)
    
    def test_addOneTasks(self):
        tasks = Tasks("School")
        tasks.addTask(Tasks("Work"))

        self.assertEqual(self.count_elem(tasks.getTasks()), 1)
        self.assertEqual(tasks.getTasks()[0].getDescription(), "Work")
        self.assertEqual(tasks.getTasks()[0].getPrio(), 1)

    def test_addMultipleTask(self):
        tasks = Tasks("School")
        tasks.addTask(Task("Math 300 Homework"))
        tasks.addTask(Task("Math 317 Homework", 2))

        self.assertEqual(self.count_elem(tasks.getTasks()), 2)
        self.assertEqual(tasks.getTasks()[0].getDescription(), "Math 300 Homework")
        self.assertEqual(tasks.getTasks()[0].getPrio(), 1)
        self.assertEqual(tasks.getTasks()[1].getDescription(), "Math 317 Homework")
        self.assertEqual(tasks.getTasks()[1].getPrio(), 2)

    def test_addMultipleTasks(self):
        tasks = Tasks("School")
        tasks.addTask(Tasks("Morning Class"))
        tasks.addTask(Tasks("Afternoon Class"))
        
        self.assertEqual(self.count_elem(tasks.getTasks()), 2)
        self.assertEqual(self.count_elem(tasks.getTasks()[0].getTasks()), 0)
        self.assertEqual(tasks.getTasks()[0].getDescription(), "Morning Class")
        self.assertEqual(self.count_elem(tasks.getTasks()[1].getTasks()), 0)
        self.assertEqual(tasks.getTasks()[1].getDescription(), "Afternoon Class")


    def test_addTaskInTasks(self):
        tasks = Tasks("School")
        tasks.addTask(Tasks("Morning Class"))
        tasks.getTasks()[0].addTask(Task("Math 300"))

        self.assertEqual(tasks.getDescription(), "School")
        self.assertEqual(self.count_elem(tasks.getTasks()), 1)
        self.assertEqual(tasks.getTasks()[0].getDescription(), "Morning Class")
        self.assertEqual(tasks.getTasks()[0].getTasks()[0].getDescription(), "Math 300")

    def test_removeOneTask(self):
        tasks = Tasks("School")
        task = Task("Math 300 Homework")
        tasks.addTask(task)
        tasks.removeTask(task)

        self.assertEqual(self.count_elem(tasks.getTasks()), 0)

    def test_removeMultipleTask(self):
        tasks = Tasks("School")
        task = Task("Math 300 Homework")
        task1 = Task("Math 317 Homework")
        task2 = Task("CPSC 210 Homework")
        tasks.addTask(task)
        tasks.addTask(task1)
        tasks.addTask(task2)

        tasks.removeTask(task)
        tasks.removeTask(task1)

        self.assertEqual(self.count_elem(tasks.getTasks()), 1)

    def test_removeOneTasks(self):
        tasks = Tasks("School")
        tasks1 = Tasks("Morning Classes")
        tasks.addTask(tasks1)
        tasks.removeTask(tasks1)

        self.assertEqual(self.count_elem(tasks.getTasks()), 0)

    def test_removeMultipleTasks(self):
        tasks = Tasks("School")
        tasks1 = Tasks("Morning Classes")
        tasks2 = Task("Afternoon Classes")
        tasks3 = Task("Evening Classes")
        tasks.addTask(tasks1)
        tasks.addTask(tasks2)
        tasks.addTask(tasks3)

        tasks.removeTask(tasks1)
        tasks.removeTask(tasks3)

        self.assertEqual(self.count_elem(tasks.getTasks()), 1)
        self.assertEqual(tasks.getTasks()[0], tasks2)


    def test_refreshOneElement(self):
        tasks = Tasks("School")
        task = Task("Math 300 Homework")
        tasks.addTask(task)
        tasks.refresh()

        self.assertEqual(tasks.getTasks()[0], task)
        self.assertEqual(tasks.getTasks()[0].getDescription(), "Math 300 Homework")
        self.assertEqual(tasks.getTasks()[0].getPrio(), 1)
        self.assertFalse(tasks.getTasks()[0].getFinished())

    def test_refreshMultipleElement(self):
        tasks = Tasks("School")
        task = Task("Math 300 Homework")
        task1 = Task("Math 317 Homework", 3)
        task2 = Task("CPSC 210 Homework", 2)
        tasks.addTask(task)
        tasks.addTask(task1)
        tasks.addTask(task2)
        tasks.refresh()

        self.assertEqual(tasks.getTasks()[0], task)
        self.assertEqual(tasks.getTasks()[1], task2)
        self.assertEqual(tasks.getTasks()[2], task1)


if __name__ == "__main__":
    unittest.main()