from cm_sdk.models import CloudManagerBase, CloudManagerEnum


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

    All consructors expect key-word style arguments.

    """

    def __init__(self, id=None, group_id=None, type_name=None,
                 event_type_name=None, enabled=False,
                 matchers=None, notifications=None):
        self.group_id = group_id
        self.type_name = type_name
        self.event_type_name = event_type_name
        self.enabled = enabled
        self.matchers = matchers if matchers else []
        self.notifications = notifications if notifications else []
        self.debug = []

    @property
    def matchers(self):
        return self._matchers

    @matchers.setter
    def matchers(self, matchers):

        _matchers = []

        for matcher in matchers:

            if isinstance(matcher, Matcher):
                self._matchers = _matchers.append(matcher)
            else:
                _m = Matcher.from_dict(matcher)
                _matchers.append(_m)
                self.debug.append(type(_m))

        self._matchers = _matchers


    @property
    def notifications(self):
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):

        _notifications = []

        for notification in notifications:

            if isinstance(notification, Notification):
                _notifications.append(notification)
            else:
                _n = Notification.from_dict(notification)
                _notifications.append(_n)
                self.debug.append(type(_n))

        self._notifications = _notifications


    class TypeName(CloudManagerEnum):
        HOST = "HOST"
        HOST_METRIC = "HOST_METRIC"
        AGENT = "AGENT"
        BACKUP = "BACKUP"
        GROUP = "GROUP"
        REPLICA_SET = "REPLICA_SET"
        USER = "USER"

    class EventTypeName(CloudManagerBase):

        class HOST(CloudManagerEnum):
            HOST_DOWN = "HOST_DOWN"
            HOST_RECOVERING = "HOST_RECOVERING"
            VERSION_BEHIND = "VERSION_BEHIND"
            HOST_EXPOSED = "HOST_EXPOSED"

        class HOST_METRIC(CloudManagerEnum):
            OUTSIDE_METRIC_THRESHOLD = "OUTSIDE_METRIC_THRESHOLD"

        class AGENT(CloudManagerEnum):
            MONITORING_AGENT_DOWN = "MONITORING_AGENT_DOWN"
            MONITORING_AGENT_VERSION_BEHIND = "MONITORING_AGENT_VERSION_BEHIND"
            BACKUP_AGENT_DOWN = "BACKUP_AGENT_DOWN"
            BACKUP_AGENT_VERSION_BEHIND = "BACKUP_AGENT_VERSION_BEHIND"
            BACKUP_AGENT_CONF_CALL_FAILURE = "BACKUP_AGENT_CONF_CALL_FAILURE"

        class BACKUP(CloudManagerEnum):
            OPLOG_BEHIND = "OPLOG_BEHIND"
            CLUSTER_MONGOS_IS_MISSING = "CLUSTER_MONGOS_IS_MISSING"
            RESYNC_REQUIRED = "RESYNC_REQUIRED"
            RS_BIND_ERROR = "RS_BIND_ERROR"
            BACKUP_TOO_MANY_RETRIES = "BACKUP_TOO_MANY_RETRIES"
            BACKUP_IN_UNEXPECTED_STATE = "BACKUP_IN_UNEXPECTED_STATE"
            LATE_SNAPSHOT = "LATE_SNAPSHOT"
            BAD_CLUSTERSHOTS = "BAD_CLUSTERSHOTS"
            SYNC_SLICE_HAS_NOT_PROGRESSED = "SYNC_SLICE_HAS_NOT_PROGRESSED"

        class GROUP(CloudManagerEnum):
            USERS_AWAITING_APPROVAL = "USERS_AWAITING_APPROVAL"
            USERS_WITHOUT_MULTI_FACTOR_AUTH = "USERS_WITHOUT_MULTI_FACTOR_AUTH"

        class REPLICA_SET(CloudManagerEnum):
            CONFIGURATION_CHANGED = "CONFIGURATION_CHANGED"
            PRIMARY_ELECTED = "PRIMARY_ELECTED"
            TOO_FEW_HEALTHY_MEMBERS = "TOO_FEW_HEALTHY_MEMBERS"
            TOO_MANY_UNHEALTHY_MEMBERS = "TOO_MANY_UNHEALTHY_MEMBERS"
            NO_PRIMARY = "NO_PRIMARY"
            RESYNC_REQUIRED = "RESYNC_REQUIRED"

        class USER(CloudManagerEnum):
            JOINED_GROUP = "JOINED_GROUP"
            REMOVED_FROM_GROUP = "REMOVED_FROM_GROUP"


class Matcher(CloudManagerBase):
    def __init__(self, field_name=None, operator=None, value=None):
        self.field_name = field_name
        self.operator = operator
        self.value = value

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
        # PRIMARY = "PRIMARY"
        # SECONDARY = "SECONDARY"
        # STANDALONE = "STANDALONE"
        # CONFIG = "CONFIG"
        # MONGOS = "MONGOS"


class Notification(CloudManagerBase):
    def __init__(self, type_name=None, interval_min=None, delay_min=None,
                 group_id=None, group_name=None, email_enabled=None,
                 sms_enabled=None, username=None, email_address=None,
                 mobile_number=None, notification_token=None, room_name=None,
                 channel_name=None, api_token=None, org_name=None,
                 flow_name=None, flowdock_api_token=None, service_key=None):
        self.type_name = type_name
        self.interval_min = interval_min
        self.delay_min = delay_min
        self.group_id = group_id
        self.group_name = group_name
        self.email_enabled = email_enabled
        self.sms_enabled = sms_enabled
        self.username = username
        self.email_address = email_address
        self.mobile_number = mobile_number
        self.notification_token = notification_token
        self.room_name = room_name
        self.channel_name = channel_name
        self.api_token = api_token
        self.org_name = org_name
        self.flow_name = flow_name
        self.flowdock_api_token = flowdock_api_token
        self.service_key = service_key

    class TypeName(CloudManagerEnum):
        GROUP = "GROUP"
        USER = "USER"
        SNMP = "SNMP"
        EMAIL = "EMAIL"
        SMS = "SMS"
        HIPCHAT = "HIPCHAT"
        SLACK = "SLACK"
        FLOWDOCK = "FLOWDOCK"
        PAGER_DUTY = "PAGER_DUTY"


class MetricThreshold(CloudManagerBase):
    def __init__(self, metric_name=None, mode=None, operator=None, threshold=None, units=None):
        self.metric_name = metric_name
        self.mode = mode
        self.operator = operator
        self.threshold = threshold
        self.units = units

    class Operator(CloudManagerEnum):
        GREATER_THAN = "GREATER_THAN"
        LESS_THAN = "LESS_THAN"

    class MetricThresholdUnits(CloudManagerEnum):
        RAW = "RAW"
        BITS = "BITS"
        BYTES = "BYTES"
        KILOBITS = "KILOBITS"
        KILOBYTES = "KILOBYTES"
        MEGABITS = "MIGABITS"
        MEGABYTES = "MEGABYTES"
        GIGABITS = "GIGABITS"
        GIGABYTES = "GIGABYTES"
        TERABYTES = "TERABYTES"
        PETABYTES = "PETABYTES"
        MILLISECONDS = "MILLISECONDS"
        SECONDS = "SECONDS"
        MINUTES = "MINUTES"
        HOURS = "HOURS"
        DAYS = "DAYS"

    class MetricThresholdMode(CloudManagerEnum):
        AVERAGE = "AVERAGE"
        TOTAL = "TOTAL"
