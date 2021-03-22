from src.dataFetchers.iexDamDataFetcher import getIexDamData
from src.typeDefs.fileInfo import IFileInfo
import datetime as dt
from typing import List
from src.typeDefs.iexDamRecord import IIexDamDataRecord
import os
import pandas as pd


def getExcelFilePath(fileInfo: IFileInfo, targetMonth: dt.datetime) -> str:

    targetDateStr = ''
    if not pd.isna(fileInfo['format']):
        targetDateStr = dt.datetime.strftime(targetMonth, fileInfo['format'])

    targetFilename = fileInfo['filename'].replace('{{dt}}', targetDateStr)
    targetFilePath = os.path.join(fileInfo['folder_location'], targetFilename)
    return targetFilePath


def getIexDamDataHandler(targetFilePath: str) -> List[IIexDamDataRecord]:
    return getIexDamData(targetFilePath)
