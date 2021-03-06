import pandas as pd
import datetime as dt
from typing import Dict
from typing import List
from src.typeDefs.pxiRtmRecord import IPxiRtmDataRecord

def getPxiRtmData(targetFilePath: str) -> List[IPxiRtmDataRecord]:
    dataSheetDf =pd.read_csv(targetFilePath)
    dataSheetDf=dataSheetDf.dropna(axis=1,how='all')
    dataSheetDf.drop(['Session ID','Hour'],axis=1,inplace=True)
    dataSheetDf[['Hrs','Sec']]=dataSheetDf['Time Block'].str.split('-',expand=True)
    dataSheetDf['Delivery Date'] = pd.to_datetime(dataSheetDf['Delivery Date'], format='%d-%m-%Y')
    dataSheetDf['Hrs'] = pd.to_datetime(dataSheetDf['Hrs']).dt.time
    new_ind = []
    tms = dataSheetDf['Hrs']
    dates=dataSheetDf['Delivery Date']
    for x in range(0, len(dates)):
        n = dates[x]+dt.timedelta(hours=tms[x].hour, minutes=tms[x].minute)
        new_ind.append(n)
    dataSheetDf['Delivery Date'] = new_ind
    tms = new_ind
    delta = dt.timedelta(minutes = 15)
    if len(tms)==96:
        for x in range(1,len(tms)):
            if (tms[x]==tms[x-1]+ delta):
                continue
            else:
                tms[x]=tms[x-1]+ delta
    else:
        print("Error:time Block count must be 96")
    dataSheetDf['Delivery Date'] = tms
    dataSheetDf.drop(['Sec','Time Block','Hrs'],axis=1,inplace=True)
    dataSheetDf = pd.melt(dataSheetDf, id_vars=['Delivery Date'])
    dataSheetDf = dataSheetDf.rename(columns={'variable': 'metric_name', 'value': 'data_val','Delivery Date': 'date_time'})
    for i in range(len(dataSheetDf['data_val'])):
        if (type(dataSheetDf['data_val'][i]) != float ) and (type(dataSheetDf['data_val'][i]) != int ):
            dataSheetDf['data_val'][i] = 0
    dataSheetDf['data_val'] = dataSheetDf['data_val'].astype('float64')
    dataSheetDf = dataSheetDf.drop_duplicates(
        subset=['date_time', 'metric_name'], keep='last', ignore_index=True)
    pxiRtmRecords = dataSheetDf.to_dict('records')
    return pxiRtmRecords
