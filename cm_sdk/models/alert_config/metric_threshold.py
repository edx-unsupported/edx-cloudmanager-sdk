import cm_sdk.models.alert.metric
from cm_sdk.models.common.common import CloudManagerBase, CloudManagerEnum

__author__ = 'e0d'


class Operator(CloudManagerEnum):
    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"


class Units(CloudManagerEnum):
    RAW = "RAW"
    BITS = "BITS"
    BYTES = "BYTES"
    KILOBITS = "KILOBITS"
    KILOBYTES = "KILOBYTES"
    MEGABITS = "MEGABITS"
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


class Mode(CloudManagerEnum):
    AVERAGE = "AVERAGE"
    TOTAL = "TOTAL"


class MetricThreshold(CloudManagerBase):

    children = {'metric_name': {'class':cm_sdk.models.alert.metric.MetricName},
                'mode': {'class':Mode},
                'operator': {'class':Operator},
                'units': {'class':Units},
                }
    my_api_attributes = ['metric_name', 'mode', 'operator', 'threshold', 'units']

    def __init__(self, metric_name=None, mode=None, operator=None, threshold=None, units=None):
        CloudManagerBase.__init__(self, self.my_api_attributes)
        self.metric_name = metric_name
        self.mode = mode
        self.operator = operator
        self.threshold = threshold
        self.units = units
