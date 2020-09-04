import unittest
from front_end.student_management import *


class Test_search(unittest.TestCase):
    def setUp(self):
        e1 = [1, 'nabin', 'sharma', 'male', 'computing', '1-09-2000', '9852563214', 'nabinsh@gmail.com',
              'sunil sharma', '9812556842', 'nuwakot']
        e2 = [31, 'ram', 'thapa', 'Male', '2-05-2000', '9843158763', 'samthda@gmail.com', 'shyam', '9841557963',
              'ktm']
        self.data = [e1, e2]

    def test_search(self):
        search_value = 'ram'
        index = 1
        expect = [[31, 'ram', 'thapa', 'Male', '2-05-2000', '9843158763', 'samthda@gmail.com', 'shyam', '9841557963',
                   'ktm']]
        actual = student.search(self.data, search_value, index)
        self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main()
