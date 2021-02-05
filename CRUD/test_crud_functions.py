from unittest import TestCase
import crud_functions
import csv

class Test_CRUD(TestCase):
    def test_show_table(self):
        a = 1
        b = 1
        self.assertEqual(a, b)


class Test(TestCase):
    def test_add(self):
#        table =  data_manager.get_table_from_file('csv_for_test.csv')
        table = [['test 1', 'test 2', 'test 3', 'test 4', 'test 5', 'test 6'],
                ['data 1', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                ['data 1', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                ['data 1', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                ['data 1', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6']]
        test = ['test 1', 'test 2', 'test 3', 'test 4', 'test 5', 'test 6']

        table_list = ["name", "budget_donne", "budget_restant"]
        name_file = 'csv_for_test.csv'
        result = crud_functions.add(table, table_list, name_file, test = test)
        expected_result = [['test 1', 'test 2', 'test 3', 'test 4', 'test 5', 'test 6'],
                        ['data 1', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                        ['data 1', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                        ['data 1', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                        ['data 1', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                        ['test 1', 'test 2', 'test 3', 'test 4', 'test 5', 'test 6']]
        self.assertEqual(result, expected_result)
