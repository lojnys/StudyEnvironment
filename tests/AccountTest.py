import unittest
import sys

sys.path.append("/Users/yushinnam/Desktop/python3/StudyEnvironment/model")

from Account import Account



class AccounTest(unittest.TestCase):

    def test_initPass(self):
        account = Account("abcd", "efgh", "abcd@gmail.com")

        self.assertEqual(account.getUsername(), "abcd")
        self.assertEqual(account.getPassword(), "efgh")
        self.assertEqual(account.getEmail(), "abcd@gmail.com")
        self.assertEqual(account.getTasks().getTasks(), [])
        self.assertFalse(account.getLogInStatus())
            

    def test_setUsername(self):
        
        account = Account("abcd", "efgh", "abcd@gmail.com")
        account.setUsername("aksj")

        self.assertEqual(account.getUsername(), "aksj")


    def test_setPassword(self):
        
        account = Account("abcd", "efgh", "abcd@gmail.com")
        account.setPassword("behs")

        self.assertEqual(account.getPassword(), "behs")
        


    def test_setEmail(self):
        
        account = Account("abcd", "efgh", "abcd@gmail.com")
        account.setEmail("qwir@gmail.com")

        self.assertEqual(account.getEmail(), "qwir@gmail.com")


    def test_logIn(self):
        account = Account("abcd", "efgh", "abcd@gmail.com")
        account.logIn()

        self.assertEqual(account.getLogInStatus(), True)



if __name__ == "__main__":
    unittest.main()