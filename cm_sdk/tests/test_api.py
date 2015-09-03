from cm_sdk.models.common.common import CloudManagerValidationException
from cm_sdk.tests.common import TestHelper

__author__ = 'e0d'

import unittest
from cm_sdk.api import cm_api


class AlertConfigAPITest(TestHelper, unittest.TestCase):

    def setUp(self):
        super(AlertConfigAPITest, self).setUp()

    def test_get_all_alert_configs(self):
        acs = self.api.get_alert_configs()
        self.assertEqual(len(acs), 4)

    def test_get_one_alert_config(self):

        ac = self.api.get_alert_config("eb08fea477f011e5befbecf4bb625d2e")
        self.assertIsInstance(ac, cm_api.alert_config.AlertConfig)

    def test_get_two_alert_config(self):
        ac = self.api.get_alert_config("eb08fea477f011e5befbecf4bb625d2e")
        self.assertIsInstance(ac, cm_api.alert_config.AlertConfig)

        n = ac.notifications

        print n[0].type_name

    def test_get_one_failure(self):
        try:
            ac = self.api.get_alert_config("f3c1a9fe77ed11e58626ecf4bb625d2e")
            self.assertIsInstance(ac, cm_api.alert_config.AlertConfig)
        except CloudManagerValidationException:
            pass
        except:
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
