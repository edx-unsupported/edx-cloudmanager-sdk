import requests

__author__ = 'e0d'

class CloudManagerAPIException(Exception):
    pass

class CloudManagerClient(object):
    """
    Simple client for interacting over HTTP with the the MongoDB
    CloudManager API.
    """

    HEADERS = {'Content-type': 'application/json'}

    def __init__(self, group_id, api_user, api_key, api_host):
        """
        A simple client for abstracting authentication and interactions over HTTP
        with the CloudManager API.

        :param group_id: CloudManager group_id
        :param api_user: CloudManager api_user
        :param api_key: CloudManager api_key associated with the provided user
        :param api_host: The endpoint host for interacting with the API
        :return: A CloudManagerClient instance
        """
        self.base_url = api_host + "/api/public/v1.0"
        self.group_id = group_id
        self.http_digest_auth = requests.auth.HTTPDigestAuth(api_user, api_key)

    def _get_final_url(self, url_template):
        return self.base_url + url_template.format(group_id=self.group_id)

    def _valid_response(self, response):
        if 'error' in response:
            raise CloudManagerAPIException(response)
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
        r = requests.put(self._get_final_url(path),
                          auth=self.http_digest_auth,
                          headers=self.HEADERS,
                          data=data)
        return self._valid_response(r.json())

    def post(self, path, data):
        # Not using the requests json keyword which expects a python dict
        # intentionally.
        r = requests.post(self._get_final_url(path),
                          auth=self.http_digest_auth,
                          headers=self.HEADERS,
                          data=data)
        return self._valid_response(r.json())

    def delete(self, path):
        """
        Delete an API object
        :param path: The path including the ID of the item to delete
        :return: Returns a boolean value indicating success or failure
        """
        r = requests.delete(self._get_final_url(path),
                            auth=self.http_digest_auth,
                            headers=self.HEADERS)
        try:
            self._valid_response(r.json())
        except CloudManagerAPIException:
            return False

        return True
