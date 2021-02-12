from typing import TypedDict
import datetime as dt


class IGenLineDataRecord(TypedDict):
    data_time: dt.datetime
    entity_tag:str
    generator_tag: str
    data_val: str