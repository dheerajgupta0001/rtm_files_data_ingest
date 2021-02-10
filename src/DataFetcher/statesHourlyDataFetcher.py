from typing import Dict
import pandas as pd 
from src.config.appConfig import getFileMappings
import datetime as dt
from src.typeDefs.fileInfo import IFileInfo 
from src.typeDefs.measRecord import IMetricsDataRecord 
import os 
from typing import List

def getStatesHourlyData(fileInfo:IFileInfo,tagetMonth:dt.datetime) -> List[IMetricsDataRecord]:
    
    targetDateStr = dt.datetime.strftime(tagetMonth , '%b_%Y')
    
    targetFilename = fileInfo['filename'].replace('{{dt}}', targetDateStr)
    targetFilePath = os.path.join(fileInfo['folder_location'], targetFilename)

    dataDf = pd.ExcelFile(targetFilePath)
    sheetNames = dataDf.sheet_names

    
    for sheet in sheetNames:
        print(sheet)
        # getSheetData(sheet)
        dataSheeetDf = pd.read_excel(targetFilePath, sheet_name=sheet, skiprows=1)
        print(dataSheeetDf)

    return


def getSheetData():
    pass



