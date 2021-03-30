from typing import Dict
import pandas as pd
import datetime as dt
from src.typeDefs.wbesRtmPxiRecord import IWbesRtmPxiDataRecord
from typing import List
import csv
import numpy as np


def getWbesRtmPxiData(targetFilePath: str, targetDt : dt.datetime) -> List[IWbesRtmPxiDataRecord]:
    wbesRtmPxiRecord: List[IWbesRtmPxiDataRecord] = []
    #  TODO
    wbesRtmPxiRecord = wbesRtmPxiDf.to_dict('records')

    return wbesRtmPxiRecord

