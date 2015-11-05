__author__ = 'e0d'

from cm_sdk.models import CloudManagerBase

class Link(CloudManagerBase):
    children = {}
    my_api_attributes = ['href', 'rel']

    def __init__(self, href = None, rel = None):
        CloudManagerBase.__init__(self, self.my_api_attributes)
        self.href = href
        self.rel = rel
