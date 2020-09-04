import unittest
from model.model_user_login import *


class test_login(unittest.TestCase):
    def setUp(self):
        self.log = login('student', 'manage')

    def test_set_user(self):
        self.log.set_user('student')
        self.assertEqual('student', self.log.get_user())

    def test_get_password(self):
        self.assertEqual('manage', self.log.get_password())


if __name__ == '__main__':
    unittest.main()
