from typing import Dict
import pandas as pd
import datetime as dt
from src.typeDefs.stateConfig import IStateConfig
from src.typeDefs.measRecord import IMetricsDataRecord
from typing import List

def getStatesDailyData(statesConfigSheet: List[IStateConfig], targetFilePath: str) -> List[List]:

    allStatesRecords = []
    stateDailyRecords: List[IMetricsDataRecord] = []
   
    for eachRow in statesConfigSheet:
        sheetName = eachRow['sheet_daily_data']
        
        # check if sheetname is not nan
        if pd.isna(sheetName):
            continue
        
        dataSheetDf = pd.read_excel(
            targetFilePath, sheet_name=sheetName, skiprows=1)
        dataSheetDf = pd.melt(dataSheetDf, id_vars=['Date'])
        dataSheetDf['entity_tag'] = eachRow['name']
        dataSheetDf = dataSheetDf.rename(columns={
            'variable': 'metric_name', 'value': 'data_val',
            'Date': 'data_time'})
        dataSheetDf['data_val'].fillna(0, inplace=True)
        # convert dataframe to list of dictionaries
        stateDailyRecords = dataSheetDf.to_dict('records')
        allStatesRecords.append(stateDailyRecords)
        
    return allStatesRecords