"""
Emailer slicer which gets the username and domain from an email
"""
import unittest


class TestInput(unittest.TestCase):

    def test_input(self):
        self.assertEqual(checkInput("m@m.co.za"), True, "Should be True")
        self.assertEqual(checkInput("mm.co.za"), False, "No @ symbol")
        self.assertEqual(checkInput("m@mcoza"), False, "No .")
        self.assertEqual(checkInput("m@m@coza"), False, "To may @ symbols")

    def test_split(self):
        self.assertEqual(splitEmail("m@m.co.za"), ("m", "m.co.za"), "Should be True")


def checkInput(email):
    if "@" not in email or "." not in email:
        return False
    elif email.count("@") > 1:
        return False
    return True


def splitEmail(email):
    username = email[:email.find("@")]
    domain = email[email.find("@")+1:]
    return username, domain


email = input("Enter an email adress: ")
while not checkInput(email):
    print("Please enter a valid email adress")
    email = input("Enter an email adress: ")

print("Username: ", splitEmail(email)[0], " and domain: ", splitEmail(email)[1])

