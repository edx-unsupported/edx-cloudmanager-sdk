from enum import Enum 
from cm_sdk.models import CommonEqualityMixin

class StatusName(Enum):
    INACTIVE = 1
    PROVISIONING = 2
    STARTED = 3
    STOPPED = 4
    TERMINATING = 5

class StorageEngine(Enum):
    MEMORY_MAPPED = 1
    WIRED_TIGER = 2

class AuthMechanismName(Enum):
    MONGODB_CR = 1
    GSSAPI = 2
    PLAIN = 3
    MONGODB_X509 = 4
    NONE = 5

class BackupConfiguration(CommonEqualityMixin):
    def __init__(self):
        pass

class Bar:
   pass    

if __name__ == "__main__":
    
    bc = BackupConfiguration()
