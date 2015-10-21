from cm_sdk.models import CommonEquivalenceMixin, CloudManagerEnum


class Alert(CommonEquivalenceMixin):
    def __init__(self, alert_id, group_id, alert_config_id,
                 type_name, event_type_name, status):
        self.id = alert_id
        self.group_id = group_id
        self.alert_config_id = alert_config_id
        self.type_name = type_name
        self.event_type_name = event_type_name
        self.status = status

    class TypeName(CloudManagerEnum):
        HOST = "HOST"
        HOST_METRIC = "HOST_METRIC"
        AGENT = "AGENT"
        BACKUP = "BACKUP"
        GROUP = "GROUP"
        REPLICA_SET = "REPLICA_SET"
        USER = "USER"
