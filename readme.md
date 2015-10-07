edx-ops CloudManager SDK
==============

A simple SDK for managaging Cloudmanager configuration in an automated way.  The implemenation is oportunistic and incomplete.

Sample Usage
--------------

```
#
# Create, fetch, delete, 404
#
import json
import pprint
from cm_sdk.models.alert_config import Notification, Matcher, AlertConfig
from cm_sdk.api.alert_config import AlertConfigApi
import cm_sdk.client

# keys and ids have been changed to representative, 
# but not reals, values
group_id = "JBAE4urukmv1GY3pukguksSZ8"
c = cm_sdk.client.CloudManagerClient("https://cloud.mongodb.com",group_id, "me@example.com","9705abe4-6d10-11e5-a3c6-ecf4bb625d2e")
api = AlertConfigApi(c)

# Create a configuration with child objects
m = Matcher(Matcher.FieldName.REPLICA_SET_NAME,Matcher.Operator.EQUALS, "rs1")

n = Notification(Notification.TypeName.EMAIL, 60, 5, email_address="me@example.org")
ac = AlertConfig(group_id=group_id, type_name=AlertConfig.TypeName.AGENT, 
                 event_type_name=AlertConfig.EventTypeName.AGENT.MONITORING_AGENT_DOWN, 
                 enabled=True, 
                 matchers=[m], 
                 notifications=[n])

created = api.create_alert_config(ac)
print "Created AlertConfig"
print created

# Fetch it back
fetched = api.get_alert_config(created['id'])
print "Fetched AlertConfig"
print fetched

# Delete it
print "Deleting AlertConfiguration with id {config_id}".format(config_id=fetched.id)
deleted = api.delete_alert_config(fetched.id)
print deleted

# Confirm it is gone
fetched = api.get_alert_config(fetched.id)
print fetched
```
