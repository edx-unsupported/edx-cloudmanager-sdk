import json
from json import JSONEncoder
import requests

class CloudManagerClient(object):
    def __init__(self, base_url, group_id, api_user, api_key):
        self.base_url = base_url + "/api/public/v1.0"
        self.group_id = group_id
        self.http_digest_auth = requests.auth.HTTPDigestAuth(api_user, api_key)

    def get(self, path):
        api_target = self.base_url + path
        r = requests.get(api_target, auth=self.http_digest_auth)
        return r.json()

    def put():
        # TODO: implement me
        pass

    def post(self, path, data):
        api_target = self.base_url + path
        return json.dumps(data, cls=MyEncoder)
        # TODO WIP
        #r = requests.post(api_target, auth=self.http_digest_auth, data=data)
        
    def delete():
        # TODO: implement me
        pass

