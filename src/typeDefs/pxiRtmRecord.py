from typing import TypedDict
import datetime as dt


class IPxiRtmDataRecord(TypedDict):
    data_time: dt.datetime
    metric_name: str
    data_val: str
