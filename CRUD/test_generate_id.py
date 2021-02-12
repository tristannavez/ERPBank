from unittest import TestCase

import data_manager, common

class Test(TestCase):

    def test_id(self):
        table = [['test1', 'test 2', 'test 3', 'test 4', 'test 5', 'test 6'],
                 ['1', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                 ['2', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                 ['3', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                 ['4', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6']]

        result = common.generate_random(table)

        expected_result = '5'

        self.assertEqual(result, expected_result)