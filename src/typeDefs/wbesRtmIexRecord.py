from typing import TypedDict
import datetime as dt


class IWbesRtmIexDataRecord(TypedDict):
    date_time: dt.datetime
    beneficiary: str
    beneficiary_type: str
    data_val: float
