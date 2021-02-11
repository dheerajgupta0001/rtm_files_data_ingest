from typing import Dict
import pandas as pd 
from src.config.appConfig import getFileMappings, getJsonConfig
import datetime as dt
from src.typeDefs.fileInfo import IFileInfo 
from src.typeDefs.measRecord import IMetricsDataRecord 
import os 
from typing import List
from src.repos.measData.measDataRepo import MeasDataRepo

def getStatesDailyData(fileInfo:IFileInfo,tagetMonth:dt.datetime, noOfRowsToSkip= int) -> bool:

    # get config details
    jsonConfig = getJsonConfig()
    targetDateStr = dt.datetime.strftime(tagetMonth , '%b_%Y')
    
    targetFilename = fileInfo['filename'].replace('{{dt}}', targetDateStr)
    targetFilePath = os.path.join(fileInfo['folder_location'], targetFilename)
    print(targetFilePath)

    dataDf = pd.ExcelFile(targetFilePath)
    sheetNames = dataDf.sheet_names
    
    records:List[IMetricsDataRecord] = []
    for sheet in sheetNames:
        print(sheet)
        if sheet == 'IR Regionwise Sch Act':
            dataSheeetDf = pd.read_excel(targetFilePath, sheet_name=sheet, skiprows=1, header=None)
            columnsData = dataSheeetDf.iloc[0]
            for itr in range(len(columnsData)):
                if itr==1 or itr == 2 or itr ==3 or itr == 4:
                    columnsData[itr] = 'East ' + columnsData[itr]
                elif itr==5 or itr == 6 or itr ==7 or itr == 8:
                    columnsData[itr] = 'North ' + columnsData[itr]
                elif itr==9 or itr == 10 or itr ==11 or itr == 12:
                    columnsData[itr] = 'South ' + columnsData[itr]
            dataSheeetDf = pd.read_excel(targetFilePath, sheet_name=sheet, skiprows=2, header=None)
            dataSheeetDf.columns = columnsData
            dataSheeetDf = pd.melt(dataSheeetDf , id_vars=['Date'])
            dataSheeetDf = dataSheeetDf.rename(columns={0: 'metric_name', 'value': 'data_val',
                                        'Date': 'data_time'})
        else:
            # getSheetData(sheet)
            dataSheeetDf = pd.read_excel(targetFilePath, sheet_name=sheet, skiprows=noOfRowsToSkip)
            dataSheeetDf = pd.melt(dataSheeetDf, id_vars=['Date'])
            dataSheeetDf = dataSheeetDf.rename(columns={
                            'variable': 'metric_name', 'value': 'data_val',
                            'Date': 'data_time'})

        dataSheeetDf['entity_tag'] = sheet
        dataSheeetDf['data_val'].fillna(0, inplace=True)
        # convert dataframe to list of dictionaries
        stateDailyRecords = dataSheeetDf.to_dict('records')
        # print(stateDailyRecords)
        # get the instance of state Hourly metrics data storage repository
        measDataRepo = MeasDataRepo(jsonConfig['appDbConnStr'])
        isRawCreationSuccess = False
        if noOfRowsToSkip == 1:
            isRawCreationSuccess = measDataRepo.insertStatesDailyData(stateDailyRecords)
            if isRawCreationSuccess:
                print("State Daily data insertion SUCCESSFUL for {}".format(sheet))
            else:
                print("State Daily data insertion UNSUCCESSFUL for {}".format(sheet))
        else:
            isRawCreationSuccess = measDataRepo.insertGenLinesDailyData(stateDailyRecords)
            if isRawCreationSuccess:
                print("Gen Lines Daily data insertion SUCCESSFUL for {}".format(sheet))
            else:
                print("Gen Lines Daily data insertion UNSUCCESSFUL for {}".format(sheet))

    return True


