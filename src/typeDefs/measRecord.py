from typing import TypedDict
import datetime as dt


class IMetricsDataRecord(TypedDict):
    data_time: dt.datetime
    entity_tag: str
    metric_name: str
    data_val: str