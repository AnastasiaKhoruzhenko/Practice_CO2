import unittest

from main import get_km_row, get_info_from_database, get_splitted_array, co2_list, app

TEST_DB = 'newDatabase.db'


class BasicTests(unittest.TestCase):

    def test_get_km_error(self):
        expected = -1
        actual = get_km_row('100')
        self.assertEqual(expected, actual, 'test \'get km with invalid value\' failed')

    def test_get_km_right(self):
        expected = 1
        actual = get_km_row('125')
        self.assertEqual(expected, actual, 'test \'get km with valid value\' failed')

    def test_right_request(self):
        with app.test_request_context('?aircraft=100,141&distance=125,500'):
            aircraft = get_splitted_array('aircraft')
            distance = get_splitted_array('distance')
            self.assertEqual(len(aircraft), 2)
            self.assertEqual(len(distance), 2)
            self.assertEqual(aircraft, ['100', '141'])


if __name__ == "__main__":
    unittest.main()
