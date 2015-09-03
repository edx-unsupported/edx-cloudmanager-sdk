from cm_sdk.models.common.common import CloudManagerBase, CloudManagerEnum


class StatusName(CloudManagerEnum):
    INACTIVE = "INACTIVE"
    PROVISIONING = "PROVISIONING"
    STARTED = "STARTED"
    STOPPED = "STOPPED"
    TERMINATING = "TERMINATING"


class StorageEngineName(CloudManagerEnum):
    MEMORY_MAPPED = "MEMORY_MAPPED"
    WIRED_TIGER = "WIRED_TIGER"


class AuthMechanismName(CloudManagerEnum):
    MONGODB_CR = "MONGO_CR"
    GSSAPI = "GSSAPI"
    PLAIN = "PLAIN"
    MONGODB_X509 = "MOGODB_X509"
    NONE = "NONE"


class BackupConfig(CloudManagerBase):

    children = {
        'status_name': {'class':StatusName},
        'storage_engine_name': {'class':StorageEngineName},
        'auth_mechanism_name': {'class':AuthMechanismName}
    }
    my_api_attributes = ['auth_mechanism_name', 'cluster_id', 'excluded_namespaces', 'password', 'provisioned',
                         'ssl_enabled', 'status_name', 'storage_engine_name', 'sync_source', 'username']

    def __init__(self, auth_mechanism_name=None, cluster_id=None, excluded_namespaces=None, password=None,
                 provisioned=None, ssl_enabled=None, status_name=None, storage_engine_name=None, sync_source=None,
                 username=None):
        CloudManagerBase.__init__(self, self.my_api_attributes)
        self.auth_mechanism_name = auth_mechanism_name
        self.cluster_id = cluster_id
        self.excluded_namespaces = excluded_namespaces
        self.password = password
        self.provisioned = provisioned
        self.ssl_enabled = ssl_enabled
        self.status_name = status_name
        self.storage_engine_name = storage_engine_name
        self.sync_source = sync_source
        self.username = username
