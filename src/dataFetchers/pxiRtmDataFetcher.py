import pandas as pd
import datetime as dt
from typing import Dict
from typing import List
from src.typeDefs.pxiRtmRecord import IPxiRtmDataRecord

def getPxiRtmData(targetFilePath: str) -> List[IPxiRtmDataRecord]:
    dataSheetDf =pd.read_csv(targetFilePath)
    dataSheetDf=dataSheetDf.dropna(axis=1,how='all')
    dataSheetDf[['Hrs','Sec']]=dataSheetDf['Time Block'].str.split('-',expand=True)
    dataSheetDf['Delivery Date'] = pd.to_datetime(dataSheetDf['Delivery Date'])
    dataSheetDf['Hrs'] = pd.to_datetime(dataSheetDf['Hrs']).dt.time
    new_ind = []
    tms = dataSheetDf['Hrs']
    dates=dataSheetDf['Delivery Date']
    for x in range(0, len(dates)):
        n = dates[x]+dt.timedelta(hours=tms[x].hour, minutes=tms[x].minute)
        new_ind.append(n)

    dataSheetDf['Delivery Date'] = new_ind
    dataSheetDf.drop(['Sec','Time Block','Hrs','Session ID','Hour'],axis=1,inplace=True)
    dataSheetDf = pd.melt(dataSheetDf, id_vars=['Delivery Date'])
    dataSheetDf = dataSheetDf.rename(columns={'variable': 'metric_name', 'value': 'data_val','Delivery Date': 'date_time'})
    pxiRtmRecords = dataSheetDf.to_dict('records')
    return pxiRtmRecords