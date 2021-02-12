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
        sheetName = eachRow['sheet_gen_data']
        
        # check if sheetname is not nan
        if pd.isna(sheetName):
            continue
        
        if sheetName == 'IR Regionwise Sch Act':
            dataSheeetDf = pd.read_excel(targetFilePath, sheet_name=sheetName, skiprows=0, header=[0,1])
            dataSheeetDf.columns = ['_'.join(x) for x in dataSheeetDf.columns]
            dataSheeetDf = pd.melt(dataSheeetDf, id_vars=['Date_Date'])
            dataSheeetDf = dataSheeetDf.rename(columns={
                            'variable': 'generator_tag', 'value': 'data_val',
                            'Date_Date': 'data_time'})
            dataSheeetDf['entity_tag'] = eachRow['name']
            dataSheeetDf = dataSheeetDf.rename(columns={
            'variable': 'metric_name', 'value': 'data_val',
            'Date': 'data_time'})
            dataSheeetDf['data_val'].fillna(0, inplace=True)

        else:
            # getSheetData(sheet)
            dataSheeetDf = pd.read_excel(targetFilePath, sheet_name=sheetName, skiprows=0)
            dataSheeetDf = pd.melt(dataSheeetDf, id_vars=['Date'])
            dataSheeetDf = dataSheeetDf.rename(columns={
                            'variable': 'generator_tag', 'value': 'data_val',
                            'Date': 'data_time'})
            dataSheeetDf['entity_tag'] = eachRow['name']
            dataSheeetDf = dataSheeetDf.rename(columns={
            'variable': 'metric_name', 'value': 'data_val',
            'Date': 'data_time'})
            dataSheeetDf['data_val'].fillna(0, inplace=True)
        # dataSheetDf = pd.read_excel(
        #     targetFilePath, sheet_name=sheetName, skiprows=1)
        # dataSheetDf = pd.melt(dataSheetDf, id_vars=['Date'])
        
        # convert dataframe to list of dictionaries
        genLineDailyRecords = dataSheeetDf.to_dict('records')
        allGenLinesRecords.append(genLineDailyRecords)
        
    return allGenLinesRecords
