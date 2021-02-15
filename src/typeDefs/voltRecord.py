from typing import TypedDict
import datetime as dt


class IVoltDataRecord(TypedDict):
    data_time: dt.datetime
    volt_level: float
    entity_name: str
    metric_name: str
    data_val: str
