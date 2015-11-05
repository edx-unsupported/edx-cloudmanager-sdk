from cm_sdk.client import CloudManagerClient
from cm_sdk.models.alert_config import alert_config
from cm_sdk.models.host import host
from cm_sdk.models.backup_config import backup_config

class Api(object):
    """
    MongoDB CloudManager API wrapper for CRUD operations on AlertConfigurations.
    https://docs.cloud.mongodb.com/reference/api/alert-configurations/

    Expected usage is as follows

    import json
    import pprint
    from cm_sdk.models.alert_config import AlertConfig
    from cm_sdk.api.alert_config import AlertConfigApi
    import cm_sdk.client

    # keys and ids have been changed to representative,
    # but not reals, values
    group_id = "JBAE4urukmv1GY3pukguksSZ8"

    c = cm_sdk.client.CloudManagerClient(
         "https://cloud.mongodb.com",
         group_id,
         "me@example.com",
         "9705abe4-6d10-11e5-a3c6-ecf4bb625d2e")

    api = AlertConfigApi(c)

    fetched = api.get_alert_configs()
    """
    IMPLEMENTED_APIS = [
        {"name": "AlertConfig", "status": "beta"},
        {"name": "Alert", "status": "alpha"},
        {"name": "BackupConfig", "status": "alpha"},
        {"name": "Host", "status": "alpha"}]


    def __init__(self, group_id, api_user, api_key, api_host="https://cloud.mongodb.com"):
        self.client = CloudManagerClient(group_id, api_user, api_key, api_host)


    def get_alert_configs(self):
        """
        Return all the CloudManager AlertConfig objects as a list of
        cm_sdk.models.alert_config.AlertConfig instances.
        """
        to_return = []

        alert_configs = self.client.get("/groups/{group_id}/alertConfigs")
        for ac in alert_configs['results']:
            to_return.append(alert_config.AlertConfig.from_dict(ac))

        return to_return


    def get_alert_config(self, config_id):
        """
        Return a single cm_sdk.models.alert_config.AlertConfig for a
        given id.
        """
        fetched = self.client.get("/groups/{group_id}" + "/alertConfigs/{config_id}"
                                  .format(config_id=config_id))
        return alert_config.AlertConfig.from_dict(fetched)


    def create_alert_config(self, to_create):
        """
        Create a new CloudManager AlertConfig
        """
        created = self.client.post("/groups/{group_id}/alertConfigs", to_create)
        return alert_config.AlertConfig.from_dict(created)


    def delete_alert_config(self, config_id):
        """
        Delete a CloudManager AlertConfig given an AlertConfig id
        """
        self.client.delete("/groups/{group_id}" + "/alertConfigs/{config_id}".format(config_id=config_id))
        return True

    #
    # Hosts
    #

    def get_hosts(self):
        """
        Return all the CloudManager Host objects as a list of
        cm_sdk.models.host.Host instances.
        """
        to_return = []

        hosts = self.client.get("/groups/{group_id}/hosts")
        for item in hosts['results']:
            to_return.append(host.Host.from_dict(item))

        return to_return


    def create_host(self, to_create):
        created = self.client.post("/groups/{group_id}/hosts", to_create)
        return host.Host.from_dict(created)


    #
    # BackupConfigs
    #

    def get_backup_configs(self):
        """
        Return all the CloudManager backupConfig objects.
        """
        to_return = []
        backup_configs = self.client.get("/groups/{group_id}/backupConfigs")

        for item in backup_configs['results']:
            to_return.append(backup_config.BackupConfig.from_dict(item))

        return to_return