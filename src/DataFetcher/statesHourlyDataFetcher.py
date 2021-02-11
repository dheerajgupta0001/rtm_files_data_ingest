from typing import Dict
import pandas as pd 
from src.config.appConfig import getFileMappings, getJsonConfig
import datetime as dt
from src.typeDefs.fileInfo import IFileInfo 
from src.typeDefs.measRecord import IMetricsDataRecord 
import os 
from typing import List
from src.repos.measData.measDataRepo import MeasDataRepo

def getStatesHourlyData(fileInfo:IFileInfo,tagetMonth:dt.datetime) -> bool:

    # get config details
    jsonConfig = getJsonConfig()
    targetDateStr = dt.datetime.strftime(tagetMonth , '%b_%Y')
    
    targetFilename = fileInfo['filename'].replace('{{dt}}', targetDateStr)
    targetFilePath = os.path.join(fileInfo['folder_location'], targetFilename)

    dataDf = pd.ExcelFile(targetFilePath)
    sheetNames = dataDf.sheet_names
    
    records:List[IMetricsDataRecord] = []
    for sheet in sheetNames:
        print(sheet)
        # getSheetData(sheet)
        dataSheeetDf = pd.read_excel(targetFilePath, sheet_name=sheet, skiprows=1)
        # make timestamp
        dataSheeetDf['Hours'] = dataSheeetDf['Hours'] - 1
        dataSheeetDf['Date'] +=  pd.to_timedelta(dataSheeetDf.Hours, unit='h')
        del dataSheeetDf['Hours']
        dataSheeetDf = pd.melt(dataSheeetDf, id_vars=['Date'])
        dataSheeetDf['entity_tag'] = sheet
        dataSheeetDf = dataSheeetDf.rename(columns={
                            'variable': 'metric_name', 'value': 'data_val',
                            'Date': 'data_time'})
        dataSheeetDf['data_val'].fillna(0, inplace=True)
        # convert dataframe to list of dictionaries
        stateHourlyRecords = dataSheeetDf.to_dict('records')
        # print(records)
        # get the instance of state Hourly metrics data storage repository
        measDataRepo = MeasDataRepo(jsonConfig['appDbConnStr'])
        isRawCreationSuccess = False
        isRawCreationSuccess = measDataRepo.insertStatesHorlyData(stateHourlyRecords)
        if isRawCreationSuccess:
            print("State Hourly data insertion SUCCESSFUL for {}".format(sheet))
        else:
            print("State Hourly data insertion UNSUCCESSFUL for {}".format(sheet))
    return True


