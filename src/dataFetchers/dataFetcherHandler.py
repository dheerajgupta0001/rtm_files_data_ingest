from src.dataFetchers.statesHourlyDataFetcher import getStatesHourlyData
from src.dataFetchers.statesDailyDataFetcher import getStatesDailyData
from src.dataFetchers.linesGenDailyDataFetcher import getGenLinesDailyData
from src.dataFetchers.reservoirDailyDataFetcher import getReservoirDailyData
from src.dataFetchers.gujREDailyDataFetcher import getGujREGenerationData
from src.typeDefs.fileInfo import IFileInfo
from src.typeDefs.stateConfig import IStateConfig
import datetime as dt
from typing import List
from src.typeDefs.measRecord import IMetricsDataRecord
from src.typeDefs.stateslinesMeasRecord import IGenLineDataRecord
from src.typeDefs.reservoirMeasRecord import IReservoirDataRecord
import os
import pandas as pd

def getExcelFilePath(fileInfo:IFileInfo, targetMonth:dt.datetime) -> str:
    
    targetDateStr = ''
    if not pd.isna(fileInfo['format']): 
        targetDateStr = dt.datetime.strftime(targetMonth , fileInfo['format'])
    
    targetFilename = fileInfo['filename'].replace('{{dt}}', targetDateStr)
    targetFilePath = os.path.join(fileInfo['folder_location'], targetFilename)
    return targetFilePath

def statesHourlyDataFetcherHandler(statesConfigSheet: List[IStateConfig], targetFilePath: str) -> List[IMetricsDataRecord]:
    return getStatesHourlyData(statesConfigSheet, targetFilePath)

def statesDailyDataFetcherHandler(statesConfigSheet: List[IStateConfig], targetFilePath: str) -> List[IMetricsDataRecord]:
    return getStatesDailyData(statesConfigSheet, targetFilePath)

def linesGenDataFetcherHandler(statesConfigSheet:List[IStateConfig], targetFilePath: str) -> List[IGenLineDataRecord]:
    return getGenLinesDailyData(statesConfigSheet , targetFilePath)
    
def reservoirDataFetcherHandler(targetFilePath: str) -> List[IReservoirDataRecord]:
    return getReservoirDailyData(targetFilePath)

def gujREGenerationDataFetcherHandler(targetFilePath: str) -> List[List[IMetricsDataRecord]]:
    return getGujREGenerationData(targetFilePath)