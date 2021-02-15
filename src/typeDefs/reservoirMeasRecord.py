from typing import TypedDict
import datetime as dt


class IReservoirDataRecord(TypedDict):
    data_time: dt.datetime
    entity_tag:str
    metric_tag: str
    data_val: str