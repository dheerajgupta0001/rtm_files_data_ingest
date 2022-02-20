from typing import Dict
import pandas as pd
import datetime as dt
from src.typeDefs.iexGdamRecord import IIexGdamDataRecord
from typing import List


def getIexGdamData(targetFilePath: str) -> List[IIexGdamDataRecord]:
    iexGdamRecords: List[IIexGdamDataRecord] = []

    excelDateDf = pd.read_excel(
        targetFilePath, sheet_name="MarketMinute", skiprows= 5, nrows= 96)
    dateValue = excelDateDf['Date | Hour | Time Block'][1]
    iexGdamDf = pd.read_excel(
        targetFilePath, sheet_name="MarketMinute", skiprows= 5, nrows= 96, header=[0,1])

    dropCols = [0,1,4,6,7,8,10,11,12,14,15,16,17,18,19,21,22,23,25,26,27]
    iexGdamDf.drop(iexGdamDf.columns[dropCols],axis=1,inplace=True)
    iexGdamDf.columns = iexGdamDf.columns.droplevel(1)
    iexGdamDf = iexGdamDf.rename(columns={
                            'Date | Hour | Time Block':"time_block"})
    iexGdamDf = iexGdamDf.loc[:, ~iexGdamDf.columns.duplicated()]
    iexGdamDf[['first_block','First','last_block']] = iexGdamDf.time_block.str.split(" ",expand=True)
    # iexGdamDf[['First','Last']] = iexGdamDf.time_block.str.split(expand=True)
    iexGdamDf = iexGdamDf.drop(['First', 'last_block', 'time_block'], axis=1)
    iexGdamDf[['hour','minute']] = iexGdamDf.first_block.str.split(":",expand=True)
    iexGdamDf['Date'] = dateValue
    iexGdamDf[['day','month','year']] = iexGdamDf.Date.str.split("-",expand=True)
    iexGdamDf['Date'] = pd.to_datetime(iexGdamDf[['year', 'month', 'day', 'hour', 'minute']])
    iexGdamDf = iexGdamDf.drop(['year', 'month', 'day', 'first_block','hour','minute'], axis=1)
    iexGdamDf = pd.melt(iexGdamDf, id_vars=['Date'])
    iexGdamDf = iexGdamDf.rename(columns={'Date': 'date_time', 'value': 'data_val',
                        'variable': 'metric_name'})
    iexGdamDf['data_val'].fillna(0, inplace=True)
    for i in range(len(iexGdamDf['data_val'])):
        if (type(iexGdamDf['data_val'][i]) != float ) and (type(iexGdamDf['data_val'][i]) != int ):
            iexGdamDf['data_val'][i] = 0
    iexGdamDf['data_val'] = iexGdamDf['data_val'].astype('float64')
    iexGdamRecords = iexGdamDf.to_dict('records')
    return iexGdamRecords
