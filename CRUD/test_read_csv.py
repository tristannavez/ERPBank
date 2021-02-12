from unittest import TestCase
import data_manager, common

class Test(TestCase):

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