from cm_sdk.models import CloudManagerBase, CloudManagerEnum

__author__ = 'e0d'

class Operator(CloudManagerEnum):
    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    CONTAINS = "CONTAINS"
    NOT_CONTAINS = "NOT_CONTAINS"
    STARTS_WITH = "STARTS_WITH"
    ENDS_WITH = "ENDS_WITH"
    REGEX = "REGEX"

class FieldName(CloudManagerEnum):
    HOSTNAME = "HOSTNAME"
    PORT = "PORT"
    HOSTNAME_AND_PORT = "HOSTNAME_AND_PORT"
    REPLICA_SET_NAME = "REPLICA_SET_NAME"
    TYPE_NAME = "TYPE_NAME"
    SHARD_NAME = "SHARD_NAME"
    CLUSTER_NAME = "CLUSTER_NAME"


class Matcher(CloudManagerBase):

    children = {
        'field_name': {'class': FieldName},
        'operator': {'class': Operator}
    }
    my_api_attributes = ['field_name', 'operator', 'value']

    def __init__(self, field_name=None, operator=None, value=None):
        CloudManagerBase.__init__(self, self.my_api_attributes)
        self.field_name = field_name
        self.operator = operator
        self.value = value

