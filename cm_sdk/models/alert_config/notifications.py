from cm_sdk.models.common.common import CloudManagerBase, CloudManagerEnum

__author__ = 'e0d'

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
    WEBHOOK = "WEBHOOK"

class Notification(CloudManagerBase):

    children = {'type_name': {'class':TypeName}}

    my_api_attributes = ['type_name', 'interval_min', 'delay_min', 'group_id',
                 'group_name', 'email_enabled', 'sms_enabled', 'username',
                 'email_address', 'mobile_number', 'notification_token',
                 'room_name', 'channel_name', 'api_token', 'org_name', 'flow_name',
                         'flowdock_api_token', 'service_key', 'roles']

    def __init__(self, type_name=None, interval_min=None, delay_min=None,
                 group_id=None, group_name=None, email_enabled=None,
                 sms_enabled=None, username=None, email_address=None,
                 mobile_number=None, notification_token=None, room_name=None,
                 channel_name=None, api_token=None, org_name=None,
                 flow_name=None, flowdock_api_token=None, service_key=None):
        CloudManagerBase.__init__(self, self.my_api_attributes)
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

