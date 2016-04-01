from cm_sdk.models.alert_config.matcher import Matcher
from cm_sdk.models.alert_config.notifications import Notification
from cm_sdk.models.alert_config.metric_threshold import MetricThreshold
from cm_sdk.models.common.common import CloudManagerBase, CloudManagerEnum
from cm_sdk.models.common.link import Link
from cm_sdk.models.alert.alert import TypeName

name_map = {"type_name":"TypeName"}


class EventTypeName(CloudManagerEnum):
    HOST_DOWN = "HOST_DOWN"
    HOST_RECOVERING = "HOST_RECOVERING"
    VERSION_BEHIND = "VERSION_BEHIND"
    HOST_EXPOSED = "HOST_EXPOSED"
    OUTSIDE_METRIC_THRESHOLD = "OUTSIDE_METRIC_THRESHOLD"
    MONITORING_AGENT_DOWN = "MONITORING_AGENT_DOWN"
    MONITORING_AGENT_VERSION_BEHIND = "MONITORING_AGENT_VERSION_BEHIND"
    BACKUP_AGENT_DOWN = "BACKUP_AGENT_DOWN"
    BACKUP_AGENT_VERSION_BEHIND = "BACKUP_AGENT_VERSION_BEHIND"
    BACKUP_AGENT_CONF_CALL_FAILURE = "BACKUP_AGENT_CONF_CALL_FAILURE"
    OPLOG_BEHIND = "OPLOG_BEHIND"
    CLUSTER_MONGOS_IS_MISSING = "CLUSTER_MONGOS_IS_MISSING"
    RESYNC_REQUIRED = "RESYNC_REQUIRED"
    RS_BIND_ERROR = "RS_BIND_ERROR"
    BACKUP_TOO_MANY_RETRIES = "BACKUP_TOO_MANY_RETRIES"
    BACKUP_IN_UNEXPECTED_STATE = "BACKUP_IN_UNEXPECTED_STATE"
    LATE_SNAPSHOT = "LATE_SNAPSHOT"
    BAD_CLUSTERSHOTS = "BAD_CLUSTERSHOTS"
    SYNC_SLICE_HAS_NOT_PROGRESSED = "SYNC_SLICE_HAS_NOT_PROGRESSED"
    USERS_AWAITING_APPROVAL = "USERS_AWAITING_APPROVAL"
    USERS_WITHOUT_MULTI_FACTOR_AUTH = "USERS_WITHOUT_MULTI_FACTOR_AUTH"
    CONFIGURATION_CHANGED = "CONFIGURATION_CHANGED"
    PRIMARY_ELECTED = "PRIMARY_ELECTED"
    TOO_FEW_HEALTHY_MEMBERS = "TOO_FEW_HEALTHY_MEMBERS"
    TOO_MANY_UNHEALTHY_MEMBERS = "TOO_MANY_UNHEALTHY_MEMBERS"
    NO_PRIMARY = "NO_PRIMARY"
    RESYNC_REQUIRED = "RESYNC_REQUIRED"
    JOINED_GROUP = "JOINED_GROUP"
    REMOVED_FROM_GROUP = "REMOVED_FROM_GROUP"
    CREDIT_CARD_ABOUT_TO_EXPIRE = "CREDIT_CARD_ABOUT_TO_EXPIRE"
    INCONSISTENT_BACKUP_CONFIGURATION = "INCONSISTENT_BACKUP_CONFIGURATION"
    DELINQUENT = "DELINQUENT"


class AlertConfig(CloudManagerBase):
    """
    Class and sub-classes for representing MongoDB CloudManager API objects in python.
    
    https://docs.cloud.mongodb.com/reference/api/alert-configurations/

    Child objects are represented and nested classes and enums are
    used to represent sets of contrained values from the APIs
    perspective.

    In cases where child object need to be de-serialized from JSON
    automatically, @property and @.setter methods will need to be
    provided.

    All constructors expect key-word style arguments.

    """

    my_api_attributes = ['type_name', 'event_type_name', 'enabled', 'matchers', 'notifications', 'updated', 'links',
                         'created', 'metric_threshold', 'threshold']

    children = {'matchers': {'class':Matcher},
                'notifications':{'class':Notification},
                'type_name': {'class':TypeName},
                'event_type_name': {'class':EventTypeName},
                'metric_threshold': {'class':MetricThreshold},
                'links': {'class':Link}
                }

    def __init__(self, id=None, group_id=None, type_name=None,
                 event_type_name=None, enabled=False,
                 matchers=None, notifications=None, metric_threshold=None):
        CloudManagerBase.__init__(self, self.my_api_attributes)
        self.group_id = group_id
        self.type_name = type_name
        self.event_type_name = event_type_name
        self.enabled = enabled
        self.matchers = matchers if matchers is not None else []
        self.notifications = notifications if notifications is not None else []
        self.metric_threshold = metric_threshold
