from typing import TypedDict
import datetime as dt


class IIexGtamDataRecord(TypedDict):
    date_time: dt.datetime
    metric_name: str
    contract_type: str
    instrument_name: str
    data_val: float
