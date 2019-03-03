import unittest
from unittest import mock

from client import get_current_exchange_rate
from converter import convert_value

TEST_EXCHANGE_RATE = 10


class ConverterTestCase(unittest.TestCase):

    @mock.patch('converter.get_current_exchange_rate', return_value=TEST_EXCHANGE_RATE)
    def test_convert_value_has_right_input_value(self, _):
        self.assertEqual(convert_value(1), TEST_EXCHANGE_RATE)

    @mock.patch('converter.get_current_exchange_rate', return_value=None)
    def test_convert_value_has_not_exchange_rate(self, _):
        self.assertIsNone(convert_value(1))

    def test_get_current_exchange_rate(self):
        self.assertIsNotNone(get_current_exchange_rate())


if __name__ == '__main__':
    unittest.main()
