from enum import Enum 
from cm_sdk.models import CommonEqualityMixin

class TypeName(Enum):
    HOST = 1
    HOST_METRIC =2
    AGENT =3
    BACKUP = 4
    GROUP = 5
    REPLICA_SET = 6
    USER =7

class MatcherOperator(Enum):
    EQUALS = 1
    NOT_EQUALS = 2
    CONTAINS = 3
    NOT_CONTAINS = 4
    STARTS_WITH = 5
    ENDS_WITH = 6
    REGEX = 7

class MatcherValue(Enum):
    PRIMARY = 1
    SECONDARY = 2
    STANDALONE = 3
    CONFIG = 4
    MONGOS = 5

class NotificationTypeName(Enum):
    GROUP = 1
    USER = 2
    SNMP = 3
    EMAIL = 4
    SMS = 5
    HIPCHAT = 6
    SLACK = 7
    FLOWDOCK = 8
    PAGER_DUTY = 9

class MetricThresholdOperator(Enum):
    GREATER_THAN = 1
    LESS_THAN = 2

class MetricThresholdUnits(Enum):
    RAW = 1
    BITS = 2
    BYTES = 3
    KILOBITS = 4
    KILOBYTES = 5
    MEGABITS = 6
    MEGABYTES = 7
    GIGABITS = 8
    GIGABYTES = 9
    TERABYTES= 10
    PETABYTES = 11
    MILLISECONDS = 12
    SECONDS = 13
    MINUTES = 14
    HOURS = 15
    DAYS = 16

class MetricThresholdMode(Enum):
    AVERAGE = 1
    TOTAL = 2




class Alert(CommonEqualityMixin):
    def __init__(self, id, group_id, alert_config_id, type_name, event_type_name, status):
        self.id = id
        self.group_id = group_id
        self.alert_config_id = alert_config_id
        self.type_name = type_name
        self.event_type_name = event_type_name
        self.status = status


class AlertConfiguration(CommonEqualityMixin):
    def __init__(self, group_id, type_name, event_type_name, enabled, matchers, notifications):
        self.group_id = group_id
        self.type_name = type_name
        self.event_type_name = event_type_name
        self.enabled = enabled
        self.matchers = matchers
        self.notifications = notifications

class AlertMatcher(CommonEqualityMixin):
    def __init__(self, field_name, operator, value):
        self.field_name = field_name
        self.operator = operator
        self.value = value

class AlertNotification(object):
    def __init__(self, type_name, email_address, interval_min, delay_min):
        self.type_name = type_name;
        self.email_address = email_address
        self.interval_min = interval_min
        self.delay_min = delay_min
b
