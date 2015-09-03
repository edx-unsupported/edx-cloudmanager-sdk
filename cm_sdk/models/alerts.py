class CommonEqualityMixin(object):

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

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
