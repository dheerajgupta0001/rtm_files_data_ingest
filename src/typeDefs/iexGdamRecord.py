from typing import TypedDict
import datetime as dt


class IIexGdamDataRecord(TypedDict):
    date_time: dt.datetime
    metric_name: str
    data_val: float
