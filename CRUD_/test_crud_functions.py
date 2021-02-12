import unittest

try:
    import data_manager, common, crud_functions
except:
    from CRUD_ import common, data_manager, crud_functions


class Test(unittest.TestCase):

    def test_add(self):
        table = [['test 1', 'test 2', 'test 3', 'test 4', 'test 5', 'test 6'],
                 ['data 1', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                 ['data 1', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                 ['data 1', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                 ['data 1', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6']]

        test = ['test 1', 'test 2', 'test 3', 'test 4', 'test 5', 'test 6']

        result = crud_functions.add(table, test=test)
        expected_result = [['test 1', 'test 2', 'test 3', 'test 4', 'test 5', 'test 6'],
                           ['data 1', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                           ['data 1', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                           ['data 1', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                           ['data 1', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                           ['test 1', 'test 2', 'test 3', 'test 4', 'test 5', 'test 6']]
        self.assertEqual(result, expected_result)

    def test_remove(self):
        table = [['id1', 'test 2', 'test 3', 'test 4', 'test 5', 'test 6'],
                 ['id2', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                 ['id3', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                 ['id4', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                 ['id5', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6']]

        _id = 'id4'
        result = crud_functions.remove(table, _id, test='oui')
        expected_result = [['id1', 'test 2', 'test 3', 'test 4', 'test 5', 'test 6'],
                           ['id2', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                           ['id3', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                           ['id5', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6']]

        self.assertEqual(result, expected_result)

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

    def test_id(self):
        table = [['test1', 'test 2', 'test 3', 'test 4', 'test 5', 'test 6'],
                 ['1', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                 ['2', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                 ['3', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6'],
                 ['4', 'data 2', 'data 3', 'data 4', 'data 5', 'data 6']]

        result = common.generate_random(table)

        expected_result = '5'

        self.assertEqual(result, expected_result)

    def test_read_csv(self):
        filename = "table_test.csv"

        expected_result = [['Libelle', 'Prix', 'Quantitï¿½', 'Montant'],
                           ['1', 'Audit interne', '23000', '2', '46000'],
                           ['2', 'Suite Power BI', '400', '4', '16000'],
                           ['3', 'Formation risques credit', '1300', '3', '3900'],
                           ['4', 'Audit sï¿½curitï¿½ ', '4000', '1', '40000'],
                           ['5', 'Loyer annuel', '160000', '1', '160000'],
                           ['6', 'Provisions', '860000', '1', '860000'],
                           ['7', 'Personnel', '11500000', '1', '11500000'],
                           ['8', 'Amortissement', '12000', '1', '120000']]

        result = data_manager.get_table_from_file(filename)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
