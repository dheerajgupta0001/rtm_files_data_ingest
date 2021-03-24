from src.dataFetchers.iexDamDataFetcher import getIexDamData
from src.dataFetchers.iexGtamDataFetcher import getIexGtamData
from src.dataFetchers.iexRtmDataFetcher import getIexRtmData
from src.dataFetchers.pxiDamDataFetcher import getPxiDamData
from src.dataFetchers.wbesRtmIexFetcher import getWbesRtmIexData
from src.dataFetchers.pxiRtmDataFetcher import getPxiRtmData

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

def getIexGtamDataHandler(targetFilePath: str) -> List[IIexDamDataRecord]:
    return getIexGtamData(targetFilePath)

def getIexRtmDataHandler(targetFilePath: str) -> List[IIexDamDataRecord]:
    return getIexRtmData(targetFilePath)

def getPxiDamDataHandler(targetFilePath: str) -> List[IIexDamDataRecord]:
    return getPxiDamData(targetFilePath)

def getIexRtmDataHandler(targetFilePath: str) -> List[IIexDamDataRecord]:
    return getPxiRtmData(targetFilePath)

def getWbesRtmIexDataHandler(targetFilePath: str) -> List[IIexDamDataRecord]:
    return getWbesRtmIexData(targetFilePath)
