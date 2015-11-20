from cm_sdk.models.common.string_utils import to_camel_case, to_snake_case

__author__ = 'e0d'

import unittest


class TestCaseConversion(unittest.TestCase):

    def test_to_camel(self):

        _input = "this_is_a_test"
        expected = "thisIsATest"

        self.assertEqual(to_camel_case(_input), expected)

    def test_to_snake(self):

        _input = "thisIsATest"
        expected = "this_is_a_test"

        self.assertEqual(to_snake_case(_input), expected)

    def test_round_trip(self):

        _input = "thisIsATest"
        round_trip = to_camel_case(to_snake_case(_input))
        self.assertEqual(round_trip, _input)
