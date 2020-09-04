import unittest
from back_end.database_connection import *


# unit test
class Test_DbConnection(unittest.TestCase):
    def setUp(self):
        self.connection = DbConnection()

    # testing for value insert in database
    def test_insert(self):
        query = 'INSERT into student_manage VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        values = (
            53, 'shyam', 'Sharma', 'Male', '2-05-2000', '9852641203', 'shyamsha@gmail.com', 'Ryam', '9805264582',
            'ktm')
        self.connection.insert(query, values)
        expect = [
            (53, 'shyam', 'Sharma', 'Male', '2-05-2000', '9852641203', 'shyamsha@gmail.com', 'Ryam', '9805264582',
             'ktm')]
        actual = self.connection.select('select * from student_manage where Student_Id=53')
        self.assertEqual(expect, actual)

    # testing for update in database
    def test_update(self):
        query = 'UPDATE student_manage set First_name=%s,Last_name=%s, Gender=%s,Dob=%s,Contact=%s,' \
                'Email=%s,Parent_name=%s,Parent_contact=%s, Address=%s WHERE Student_Id=%s'
        values = ('ram', 'thapa', 'Male', '2-05-2000', '9852145687', 'ramthapasha@gmail.com', 'hari', '9632541025',
                  'ktm', 32)
        self.connection.update(query, values)
        expect = [
            (32, 'ram', 'thapa', 'Male', '2-05-2000', '9852145687', 'ramthapasha@gmail.com', 'hari', '9632541025',
             'ktm')]
        actual = self.connection.select('SELECT * from student_manage WHERE Student_Id=32')
        self.assertEqual(expect, actual)

    # testing for delete
    def test_delete(self):
        query = 'DELETE from student_manage  WHERE Student_Id=%s'
        values = (1,)
        self.connection.delete(query, values)
        expect = []
        actual = self.connection.select('SELECT * from student_manage WHERE Student_Id=1')
        self.assertEqual(expect, actual)

    # testing for select
    def test_select(self):
        query = 'INSERT into student_manage VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        values = (
            35, 'ranjit', 'sharma', 'Male', '2-05-2000', '9845216985', 'ranjitsh@gmail.com', 'shyam', '9836452784',
            'ktm')
        self.connection.insert(query, values)
        expect = [
            (35, 'ranjit', 'sharma', 'Male', '2-05-2000', '9845216985', 'ranjitsh@gmail.com', 'shyam', '9836452784',
             'ktm')]
        actual = self.connection.select('SELECT * from student_manage WHERE Student_Id=35')
        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
