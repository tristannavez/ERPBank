from unittest import TestCase
import crud_functions


class Test(TestCase):

    def test_update(self):
        table = [['id1', 'test 2', 'test 3', 'test 4', 'test 5', 'test 6'],
                 ['id2', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                 ['id3', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                 ['id4', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                 ['id5', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6']]

        _id = 'id3'
        test = [_id, 'test 2', 'test 3', 'test 4', 'test 5', 'test 6']

        result = crud_functions.update(table, _id, test=test)

        expected_result = [['id1', 'test 2', 'test 3', 'test 4', 'test 5', 'test 6'],
                           ['id2', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                           ['id3', 'test 2', 'test 3', 'test 4', 'test 5', 'test 6'],
                           ['id4', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                           ['id5', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6']]

        self.assertEqual(result, expected_result)