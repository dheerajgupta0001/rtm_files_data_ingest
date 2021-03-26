import pandas as pd
import datetime as dt
from typing import Dict
from typing import List
from src.typeDefs.iexGtamRecord import IIexGtamDataRecord

def getIexGtamData(targetFilePath: str) -> List[IIexGtamDataRecord]:
   
    dataSheetDf = pd.read_excel(targetFilePath, sheet_name="DateWiseTrade",skiprows=3)
    dataSheetDf=dataSheetDf.dropna(axis=1,how='all')
    dataSheetDf['Trade Date'].fillna(value=dataSheetDf.loc[0,'Trade Date'], inplace=True)
    dataSheetDf[['contract_type','A','B']]=dataSheetDf['Instrument Name'].str.split('-',expand=True)
    dataSheetDf.drop(['Contract Type','A','B','Opening Price','Closing/Equilibrium Price (Rs/MWh) ','Next Best Buy Bid Available','Next Best Sell Bid Available','Duration','Region','Total Traded Volume MW'],axis=1,inplace=True)
    dataSheetDf = pd.melt(dataSheetDf, id_vars=['Trade Date','Instrument Name','contract_type'])
    dataSheetDf = dataSheetDf.rename(columns={'variable': 'metric_name', 'value': 'data_val','Trade Date': 'date_time', 'Instrument Name':'instrument_name'})
    dataSheetDf['data_val'].fillna(0, inplace=True)
    for i in range(len(dataSheetDf['data_val'])):
        if dataSheetDf['data_val'][i] == '--':
            dataSheetDf['data_val'][i] = 0
    dataSheetDf['data_val'] = dataSheetDf['data_val'].astype('float64')

    iexGtamRecords = dataSheetDf.to_dict('records') 
    return iexGtamRecords

