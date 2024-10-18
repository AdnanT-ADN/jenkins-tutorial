import unittest
import greetings.messeges as greetings

class GreetingsTests(unittest.TestCase):

    def test_hi(self):
        self.assertEqual(
            greetings.hi("James", "Welcome to the test center!"),
            "Hi James! Welcome to the test center!"
        )
        self.assertEqual(
            greetings.hi("Oliver", "This is a test message."),
            "Hi Oliver! This is a test message."
        )
    
    def test_welcome(self):
        self.assertEqual(
            greetings.welcome("James", "Welcome to the test center!"),
            "Welcome James! Welcome to the test center!"
        )
        self.assertEqual(
            greetings.welcome("Oliver", "This is a test message."),
            "Welcome Oliver! This is a test message."
        )
    
    def test_hello(self):
        self.assertEqual(
            greetings.hello("James", "Welcome to the test center!"),
            "Hello James! Welcome to the test center!"
        )
        self.assertEqual(
            greetings.hello("Oliver", "This is a test message."),
            "Hello Oliver! This is a test message."
        )

if __name__ == "__main__":
    unittest.main()