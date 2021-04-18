import pandas as pd
import datetime as dt
from typing import Dict
from typing import List
from src.typeDefs.pxiDamRecord import IPxiDamDataRecord

def getPxiDamData(targetFilePath: str) -> List[IPxiDamDataRecord]:
    dataSheetDf =pd.read_csv(targetFilePath)
    # dataSheetDf = pd.read_excel(targetFilePath)

    dataSheetDf=dataSheetDf.dropna(axis=1,how='all')
    dataSheetDf[['Hrs','Sec']]=dataSheetDf['Time Slot'].str.split('-',expand=True)
    dataSheetDf['Delivery Date'] = pd.to_datetime(dataSheetDf['Delivery Date'], format='%d-%m-%Y')
    dataSheetDf['Hrs'] = pd.to_datetime(dataSheetDf['Hrs']).dt.time
    new_ind = []
    tms = dataSheetDf['Hrs']
    dates=dataSheetDf['Delivery Date']
    for x in range(0, len(dates)): 
        n = dates[x]+dt.timedelta(hours=tms[x].hour, minutes=tms[x].minute)
        new_ind.append(n)

    dataSheetDf['Delivery Date'] = new_ind
    dataSheetDf.drop(['Sec','Time Slot','Hrs'],axis=1,inplace=True)
    dataSheetDf = pd.melt(dataSheetDf, id_vars=['Delivery Date'])
    dataSheetDf = dataSheetDf.rename(columns={'variable': 'metric_name', 'value': 'data_val','Delivery Date': 'date_time'})
    dataSheetDf['data_val'].fillna(0, inplace=True)
    for i in range(len(dataSheetDf['data_val'])):
        if (type(dataSheetDf['data_val'][i]) != float ) and (type(dataSheetDf['data_val'][i]) != int ):
            dataSheetDf['data_val'][i] = 0
    dataSheetDf['data_val'] = dataSheetDf['data_val'].astype('float64')
    pxiDamRecords = dataSheetDf.to_dict('records')
    return pxiDamRecords
