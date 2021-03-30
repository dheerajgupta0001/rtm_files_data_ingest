from typing import Dict
import pandas as pd
import datetime as dt
from src.typeDefs.wbesRtmIexRecord import IWbesRtmIexDataRecord
from typing import List
import csv
import numpy as np


def getWbesRtmIexData(targetFilePath: str, targetDt : dt.datetime) -> List[IWbesRtmIexDataRecord]:
    wbesRtmIexRecord: List[IWbesRtmIexDataRecord] = []

    # TODO

    wbesRtmIexRecord = wbesRtmIexDf.to_dict('records')

    return wbesRtmIexRecord
