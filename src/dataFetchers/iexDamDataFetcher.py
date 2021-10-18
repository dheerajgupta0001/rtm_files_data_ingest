from typing import Dict
import pandas as pd
import datetime as dt
from src.typeDefs.iexDamRecord import IIexDamDataRecord
from typing import List


def getIexDamData(targetFilePath: str) -> List[IIexDamDataRecord]:
    iexDamRecords: List[IIexDamDataRecord] = []

    iexDamDf = pd.read_excel(
        targetFilePath, sheet_name="MarketMinute", skiprows= 5, nrows= 96)
    # iexDamDf = iexDamDf.rename(columns={
    #     'None.1': 'time_block', 'Date | Hour | Time Block': 'Date'})
    # iexDamDf = iexDamDf.drop([None, 'Unnamed: 4'], axis=1)
    # iexDamDf = iexDamDf.rename(columns={
    #     'Unnamed: 2': 'time_block', 'Date | Hour | Time Block': 'Date'})
    # iexDamDf = iexDamDf.drop(['Unnamed: 1', 'Unnamed: 4'], axis=1)
    iexDamDf = iexDamDf.rename(columns={
                            iexDamDf.columns[2]: "time_block", iexDamDf.columns[1]: "deleteCol",
                            'Date | Hour | Time Block': 'Date'})
    iexDamDf = iexDamDf.drop(['deleteCol', 'Unnamed: 4'], axis=1)
    iexDamDf = iexDamDf.loc[:, ~iexDamDf.columns.duplicated()]
    iexDamDf[['first_block','First','last_block']] = iexDamDf.time_block.str.split(" ",expand=True)
    # iexDamDf[['First','Last']] = iexDamDf.time_block.str.split(expand=True)
    iexDamDf = iexDamDf.drop(['First', 'last_block', 'time_block'], axis=1)
    iexDamDf[['hour','minute']] = iexDamDf.first_block.str.split(":",expand=True)
    iexDamDf['Date'] = iexDamDf['Date'][0]
    iexDamDf[['day','month','year']] = iexDamDf.Date.str.split("-",expand=True)
    iexDamDf['Date'] = pd.to_datetime(iexDamDf[['year', 'month', 'day', 'hour', 'minute']])
    iexDamDf = iexDamDf.drop(['year', 'month', 'day', 'first_block','hour','minute'], axis=1)
    iexDamDf = pd.melt(iexDamDf, id_vars=['Date'])
    iexDamDf = iexDamDf.rename(columns={'Date': 'date_time', 'value': 'data_val',
                        'variable': 'metric_name'})
    iexDamDf['data_val'].fillna(0, inplace=True)
    for i in range(len(iexDamDf['data_val'])):
        if (type(iexDamDf['data_val'][i]) != float ) and (type(iexDamDf['data_val'][i]) != int ):
            iexDamDf['data_val'][i] = 0
    iexDamDf['data_val'] = iexDamDf['data_val'].astype('float64')
    iexDamRecords = iexDamDf.to_dict('records')
    return iexDamRecords
