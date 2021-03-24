import pandas as pd
import datetime as dt
from typing import Dict
from typing import List
from src.typeDefs.iexDamRecord import IIexDamDataRecord

def getIexGtamData(targetFilePath: str) -> List[IIexDamDataRecord]:

   
    dataSheetDf = pd.read_excel(targetFilePath, sheet_name="DateWiseTrade",skiprows=3,skipfooter=0)
    dataSheetDf=dataSheetDf.dropna(axis=1,how='all')
    dataSheetDf['Trade Date'].fillna(value=dataSheetDf.loc[0,'Trade Date'], inplace=True)
    dataSheetDf['Contract Type'].fillna(value=dataSheetDf.loc[0,'Contract Type'], inplace=True)
    dataSheetDf[['Contract_Type','A','B']]=dataSheetDf['Instrument Name'].str.split('-',expand=True)
    dataSheetDf.drop(['Contract Type','A','B','Opening Price','Closing/Equilibrium Price (Rs/MWh) ','Next Best Buy Bid Available','Next Best Sell Bid Available','Duration','Region','Total Traded Volume MW'],axis=1,inplace=True)
    dataSheetDf = pd.melt(dataSheetDf, id_vars=['Trade Date','Instrument Name','Contract_Type'])
    dataSheetDf = dataSheetDf.rename(columns={'variable': 'metric_name', 'value': 'data_val','Trade Date': 'date'})
    iexGtamRecords = dataSheetDf.to_dict('records')
    return iexGtamRecords

    # print(dataSheetDf.dtypes)
    # print(dataSheetDf)

