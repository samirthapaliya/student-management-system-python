import unittest
from front_end.student_management import student


class test_sort(unittest.TestCase):
    def setUp(self):
        self.e1 = [1, 'nabin', 'sharma', 'male', '1-09-2000', '9852563214', 'nabinsh@gmail.com',
                   'sunil sharma', '9812556842', 'nuwakot']
        self.e2 = [31, 'ram', 'thapa', 'Male', '2-05-2000', '9843158763', 'samthda@gmail.com', 'shyam', '9841557963',
                   'ktm']
        self.value = [self.e1, self.e2]

    def test_sort_desc(self):
        expect = [[31, 'ram', 'thapa', 'Male', '2-05-2000', '9843158763', 'samthda@gmail.com', 'shyam', '9841557963',
                   'ktm'],
                  [1, 'nabin', 'sharma', 'male', '1-09-2000', '9852563214', 'nabinsh@gmail.com',
                   'sunil sharma', '9812556842', 'nuwakot']]
        actual = student.merge_sort(self.value, False)
        self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main()


