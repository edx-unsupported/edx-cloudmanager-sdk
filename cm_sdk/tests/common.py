import json
import httpretty
from cm_sdk.api import cm_api
from os import path

__author__ = 'e0d'

JSON_DATA = path.join(path.dirname(__file__), 'data/alertConfigs.json')

class TestHelper(object):
    def setUp(self):

        super(TestHelper, self).setUp()
        self.group_id = "7d16eb9a779611e5a957ecf4bb625d2e"
        self.principle = "user@example.com"
        self.password = "secret"
        self.alert_config_id = "53888cefe4b0d94f32b74eed"

        self.url_base = "https://cloud.mongodb.com/api/public/v1.0/groups/{group_id}".format(group_id=self.group_id)

        api = cm_api.Api(self.group_id, self.principle, self.password)
        self.api = api

        with open(JSON_DATA, 'r') as data:
            self.api_data = json.load(data)

        httpretty.enable()

        for k, v in self.api_data.iteritems():
            httpretty.register_uri(
                httpretty.GET,
                self.url_base + v['href'],
                body=json.dumps(v['response']),
                content_type="application/json")