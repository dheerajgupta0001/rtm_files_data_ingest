from typing import TypedDict
import datetime as dt


class IIexRtmDataRecord(TypedDict):
    date_time: dt.datetime
    metric_name: str
    data_val: float
