__author__ = 'edward'

import unittest
from cm_sdk.models import StringUtil as su


class TestCaseConversion(unittest.TestCase):

    def test_to_camel(self):

        _input = "this_is_a_test"
        expected = "thisIsATest"

        self.assertEqual(su.to_camel_case(_input), expected)

    def test_to_snake(self):

        _input = "thisIsATest"
        expected = "this_is_a_test"

        self.assertEqual(su.to_snake_case(_input), expected)

    def test_round_trip(self):

        _input = "thisIsATest"
        round_trip = su.to_camel_case(su.to_snake_case(_input))
        self.assertEqual(round_trip, _input)
