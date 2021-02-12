from typing import TypedDict
import datetime as dt


class IStateConfig(TypedDict):
    name: str
    sheet_daily_data: str
    sheet_hourly_data: str
    sheet_gen_data: str