from cm_sdk.models.alert_config import AlertConfig

class AlertConfigApi(object):
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
    c = cm_sdk.client.CloudManagerClient("https://cloud.mongodb.com",group_id, "me@example.com","9705abe4-6d10-11e5-a3c6-ecf4bb625d2e")
    api = AlertConfigApi(c)

    fetched = api.get_alert_configs()
    """

    def __init__(self, client):
        self.client = client


    def get_alert_configs(self):
        """
        Return all the CloudManager AlertConfig objects as a list of
        cm_sdk.models.alert_config.AlertConfig instances.
        """
        to_return = []

        alert_configs = self.client.get("/groups/{group_id}/alertConfigs")
        for alert_config in alert_configs['results']:
            to_return.append(AlertConfig.from_dict(alert_config))

        return to_return


    def get_alert_config(self, config_id):
        """
        Return a single cm_sdk.models.alert_config.AlertConfig for a
        given id.
        """
        fetched = self.client.get("/groups/{group_id}" + "/alertConfigs/{config_id}"
                                  .format(config_id=config_id))
        return AlertConfig.from_dict(fetched)


    def create_alert_config(self, to_create):
        """
        Create a new CloudManager AlertConfig
        """
        return self.client.post("/groups/{group_id}/alertConfigs", to_create)


    def delete_alert_config(self, config_id):
        """
        Delete a CloudManager AlertConfig given an AlertConfig id
        """
        return self.client.delete("/groups/{group_id}" + "/alertConfigs/{config_id}".format(config_id=config_id))
