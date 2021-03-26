import pandas as pd
import datetime as dt
from typing import Dict
from typing import List
from src.typeDefs.iexRtmRecord import IIexRtmDataRecord

def getIexRtmData(targetFilePath: str) -> List[IIexRtmDataRecord]:
    dataSheetDf = pd.read_excel(targetFilePath, sheet_name="MarketMinute",skiprows=6,skipfooter=7)
    dataSheetDf=dataSheetDf.dropna(axis=1,how='all')

    dataSheetDf['Date'].fillna(value=dataSheetDf.loc[0,'Date'], inplace=True)
    dataSheetDf[['Hrs','Sec']]=dataSheetDf['Time Block'].str.split('-',expand=True)
    dataSheetDf['Date'] = pd.to_datetime(dataSheetDf['Date'])
    dataSheetDf['Hrs'] = pd.to_datetime(dataSheetDf['Hrs']).dt.time
    new_ind = []
    tms = dataSheetDf['Hrs']
    dates=dataSheetDf['Date']
    for x in range(0, len(dates)):
        n = dates[x]+dt.timedelta(hours=tms[x].hour, minutes=tms[x].minute)
        new_ind.append(n)

    dataSheetDf['Date'] = new_ind
    dataSheetDf.drop(['Sec','Time Block','Hrs','Hour','SessionID'],axis=1,inplace=True)
    dataSheetDf = pd.melt(dataSheetDf, id_vars=['Date'])
    dataSheetDf = dataSheetDf.rename(columns={'variable': 'metric_name', 'value': 'data_val','Date': 'date_time'})

    dataSheetDf['data_val'].fillna(0, inplace=True)
    for i in range(len(dataSheetDf['data_val'])):
        if (type(dataSheetDf['data_val'][i]) != float ) and (type(dataSheetDf['data_val'][i]) != int ):
            dataSheetDf['data_val'][i] = 0
    dataSheetDf['data_val'] = dataSheetDf['data_val'].astype('float64')

    iexRtmRecords = dataSheetDf.to_dict('records')
    return iexRtmRecords