from typing import Dict
import pandas as pd
import datetime as dt
from src.typeDefs.iexDamRecord import IIexDamDataRecord
from typing import List


def getIexDamData(targetFilePath: str) -> List[IIexDamDataRecord]:
    iexDamRecords: List[IIexDamDataRecord] = []

    iexDamDf = pd.read_excel(
        targetFilePath, sheet_name="MarketMinute", skiprows= 5, nrows= 96)
    iexDamDf = iexDamDf.rename(columns={
        'Unnamed: 2': 'time_block', 'Date | Hour | Time Block': 'Date'})
    # for itr in range(iexDamDf['None.1']):
    #     iexDamDf[]
    # del iexDamDf[None]
    iexDamDf = iexDamDf.drop(['Unnamed: 1', 'Unnamed: 4'], axis=1)
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
    # iexDamDf = iexDamDf.rename(columns={
    #     'variable': 'metric_name', 'value': 'data_val',
    #     'Date': 'data_time'})
    iexDamRecords = iexDamDf.to_dict('records')

    return iexDamRecords
