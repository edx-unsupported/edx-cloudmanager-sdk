__author__ = 'edward'

import unittest
from cm_sdk.tests import TestHelper
from time import localtime


class AlertConfigAPITest(TestHelper, unittest.TestCase):

    def setUp(self):
        super(AlertConfigAPITest, self).setUp()

    def test_equivalence(self):
        ac0 = self.api.get_alert_config("eb08fea477f011e5befbecf4bb625d2e")
        ac1 = self.api.get_alert_config("eb08fea477f011e5befbecf4bb625d2e")
        self.assertTrue(ac0.equivalent(ac1))

    def test_ignoring_fields_in_equivalence(self):
        ac0 = self.api.get_alert_config("eb08fea477f011e5befbecf4bb625d2e")
        ac1 = self.api.get_alert_config("eb08fea477f011e5befbecf4bb625d2e")
        ac1.created = localtime()
        ac1.updated = localtime()
        ac1.links = []
        ac1.id = "1111111"
        self.assertTrue(ac0.equivalent(ac1))

    def test_non_equivalence(self):
        ac0 = self.api.get_alert_config("eb08fea477f011e5befbecf4bb625d2e")
        ac1 = self.api.get_alert_config("a039fe8a835f11e5ae08ecf4bb625d2e")

        self.assertFalse(ac0.equivalent(ac1))

if __name__ == '__main__':
    unittest.main()
