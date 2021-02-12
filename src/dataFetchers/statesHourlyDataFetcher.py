from typing import Dict
import pandas as pd
import datetime as dt
from src.typeDefs.stateConfig import IStateConfig
from src.typeDefs.measRecord import IMetricsDataRecord
from typing import List


<<<<<<< HEAD
def getStatesHourlyData(statesConfig: List[IStateConfig], targetFilePath: str) -> bool:
    dataDf = pd.read_excel(targetFilePath)

    records: List[IMetricsDataRecord] = []
    for sConfig in statesConfig:
        sheet = sConfig['sheet_hourly_data']
        
        # getSheetData(sheet)
        dataSheeetDf = pd.read_excel(
            targetFilePath, sheet_name=sheet, skiprows=1)
=======
def getStatesHourlyData(statesConfigSheet: List[IStateConfig], targetFilePath: str) -> List[List]:

    allStatesRecords = []
    stateHourlyRecords: List[IMetricsDataRecord] = []
   
    for eachRow in statesConfigSheet:
        sheetName = eachRow['sheet_hourly_data']
    
        dataSheetDf = pd.read_excel(
            targetFilePath, sheet_name=sheetName, skiprows=1)
>>>>>>> d8ff720006d1aef0e742837879c1577d1f81c049
        # make timestamp
        dataSheetDf['Hours'] = dataSheetDf['Hours'] - 1
        dataSheetDf['Date'] += pd.to_timedelta(dataSheetDf.Hours, unit='h')
        del dataSheetDf['Hours']
        dataSheetDf = pd.melt(dataSheetDf, id_vars=['Date'])
        dataSheetDf['entity_tag'] = eachRow['name']
        dataSheetDf = dataSheetDf.rename(columns={
            'variable': 'metric_name', 'value': 'data_val',
            'Date': 'data_time'})
        dataSheetDf['data_val'].fillna(0, inplace=True)
        # convert dataframe to list of dictionaries
        stateHourlyRecords = dataSheetDf.to_dict('records')
        allStatesRecords.append(stateHourlyRecords)
        
    return allStatesRecords
