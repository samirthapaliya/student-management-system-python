import unittest
from model.model_student import *


class test_student_manage(unittest.TestCase):
    def setUp(self):
        self.stu = student_detail(10, 'samir', 'thapaliya', 'male', '05-01-1999', '9843807070', 'samir@gmail.com',
                                  'ramesh', '1234567890', 'kathmandu')

    def test_set_Student_Id(self):
        self.stu.set_Student_Id(10)
        self.assertEqual(10, self.stu.get_Student_Id())

    def test_get_First_name(self):
        self.assertEqual('samir', self.stu.get_First_name())

    def test_set_Last_name(self):
        self.stu.set_Last_name('thapaliya')
        self.assertEqual('thapaliya', self.stu.get_Last_name())

    def test_get_Gender(self):
        self.assertEqual('male', self.stu.get_Gender())

    def test_set_Dob(self):
        self.stu.set_Dob('05-01-1999')
        self.assertEqual('05-01-1999', self.stu.get_Dob())

    def test_get_Contact(self):
        self.assertEqual('9843807070', self.stu.get_Contact())

    def test_set_Email(self):
        self.stu.set_Email('samir@gmail.com')
        self.assertEqual('samir@gmail.com', self.stu.get_Email())

    def test_get_Parent_name(self):
        self.assertEqual('ramesh', self.stu.get_Parent_name())

    def test_set_Parent_contact(self):
        self.stu.set_Parent_contact('1234567890')
        self.assertEqual('1234567890', self.stu.get_Parent_contact())

    def test_get_Parent_contact(self):
        self.assertEqual('ramesh', self.stu.get_Parent_name())

    def test_set_Address(self):
        self.stu.set_Parent_contact('kathmandu')
        self.assertEqual('kathmandu', self.stu.get_Address())


if __name__ == '__main__':
    unittest.main()
