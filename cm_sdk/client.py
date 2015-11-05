import requests
from cm_sdk.api import APIException

class CloudManagerClient(object):
    """
    Simple client for interacting over HTTP with the the MongoDB
    CloudManager API.
    """

    HEADERS = {'Content-type': 'application/json'}

    def __init__(self, api_host, group_id, api_user, api_key):
        self.base_url = api_host + "/api/public/v1.0"
        self.group_id = group_id
        self.http_digest_auth = requests.auth.HTTPDigestAuth(api_user, api_key)


    def _get_final_url(self, url_template):
        return self.base_url + url_template.format(group_id=self.group_id)


    def _valid_response(self, response):
        if 'error' in response:
            raise APIException(response['error'])
        return response


    #
    # HTTP Request methods
    #
    def get(self, path):
        r = requests.get(self._get_final_url(path), auth=self.http_digest_auth)
        return self._valid_response(r.json())


    def put(self, path, data):
        # Not using the requests json keyword which expects a python dict
        # intentionally.
        r = requests.post(self._get_final_url(path),
                          auth=self.http_digest_auth,
                          headers=self.HEADERS,
                          data=data.to_json())
        return self._valid_response(r.json())


    def post(self, path, data):
        # Not using the requests json keyword which expects a python dict
        # intentionally.
        r = requests.post(self._get_final_url(path),
                          auth=self.http_digest_auth,
                          headers=self.HEADERS,
                          data=data.to_json())
        return self._valid_response(r.json())


    def delete(self, path):
        r = requests.delete(self._get_final_url(path),
                            auth=self.http_digest_auth,
                            headers=self.HEADERS)
        return self._valid_response(r.json())
