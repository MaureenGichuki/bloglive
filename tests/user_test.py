import unittest

from app.models import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username='mimo',password='mimo123')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password is not None)

    def test_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_verify_password(self):
        self.assertTrue(self.new_user.verify_password('mimo123'))