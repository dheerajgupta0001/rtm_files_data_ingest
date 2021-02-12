from typing import Dict
import pandas as pd
import datetime as dt
from src.typeDefs.stateConfig import IStateConfig
from src.typeDefs.stateslinesMeasRecord import IGenLineDataRecord
from typing import List


def getGenLinesDailyData(statesConfigSheet: List[IStateConfig], targetFilePath: str) -> List[List]:
    
    allGenLinesRecords = []
    genLineDailyRecords: List[IGenLineDataRecord] = []
   
    for eachRow in statesConfigSheet:
        sheetName = eachRow['gen_lines_daily_data']
        
        # check if sheetname is not nan
        if pd.isna(sheetName):
            continue
        
        if sheetName == 'ir_regionwise_sch_act':
            dataSheeetDf = pd.read_excel(targetFilePath, sheet_name=sheetName, skiprows=1, header=[0,1])
            dataSheeetDf.columns = ['_'.join(x) for x in dataSheeetDf.columns]


        else:
            # getSheetData(sheet)
            dataSheeetDf = pd.read_excel(targetFilePath, sheet_name=sheetName, skiprows=1)
            dataSheeetDf = pd.melt(dataSheeetDf, id_vars=['Date'])
            dataSheeetDf = dataSheeetDf.rename(columns={
                            'variable': 'metric_name', 'value': 'data_val',
                            'Date': 'data_time'})

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
