from src.dataFetchers.statesHourlyDataFetcher import getStatesHourlyData
from src.dataFetchers.statesDailyDataFetcher import getStatesDailyData
from src.typeDefs.fileInfo import IFileInfo
from src.typeDefs.stateConfig import IStateConfig
import datetime as dt
from typing import List
from src.typeDefs.measRecord import IMetricsDataRecord
import os

def getExcelFilePath(fileInfo:IFileInfo, targetMonth:dt.datetime) -> str:
    
    targetDateStr = dt.datetime.strftime(targetMonth , fileInfo['format'])
    
    targetFilename = fileInfo['filename'].replace('{{dt}}', targetDateStr)
    targetFilePath = os.path.join(fileInfo['folder_location'], targetFilename)
    
    return targetFilePath

def statesHourlyDataFetcherHandler(statesConfigSheet: List[IStateConfig], targetFilePath: str) -> List[IMetricsDataRecord]:
    return getStatesHourlyData(statesConfigSheet, targetFilePath)

def statesDailyDataFetcherHandler(statesConfigSheet: List[IStateConfig], targetFilePath: str) -> List[IMetricsDataRecord]:
    return getStatesDailyData(statesConfigSheet, targetFilePath)
