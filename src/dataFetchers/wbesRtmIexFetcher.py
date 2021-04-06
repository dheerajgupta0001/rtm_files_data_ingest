from typing import Dict
import pandas as pd
import datetime as dt
from src.typeDefs.wbesRtmIexRecord import IWbesRtmIexDataRecord
from typing import List
import csv
import numpy as np


def getWbesRtmIexData(targetFilePath: str, targetDt : dt.datetime) -> List[IWbesRtmIexDataRecord]:
    wbesRtmIexRecord: List[IWbesRtmIexDataRecord] = []

    wbesRtmIexDf = pd.read_excel(targetFilePath,skiprows=4, skipfooter=6)
    dfCols=wbesRtmIexDf.columns.tolist()
    # print(dfCols)
    wbesRtmIexDf['date_time'] = targetDt
    wbesRtmIexDf[['Hrs','Sec']]=wbesRtmIexDf['Time Desc'].str.split('-',expand=True)

    # print('The dataframe columns are {0}'.format(colNames))
    # wbesRtmIexDf['Date '] = pd.to_datetime(wbesRtmIexDf['Date '])
    wbesRtmIexDf['Hrs'] = pd.to_datetime(wbesRtmIexDf['Hrs']).dt.time
    new_ind = []
    tms = wbesRtmIexDf['Hrs']
    dates=wbesRtmIexDf['date_time']
    for x in range(0, len(dates)):
        n = dates[x]+dt.timedelta(hours=tms[x].hour, minutes=tms[x].minute)
        new_ind.append(n)

    wbesRtmIexDf['date_time'] = new_ind
    wbesRtmIexDf.drop(['Sec','Time Block','Hrs','Time Desc','Grand Total'],axis=1,inplace=True)

    dfCols=wbesRtmIexDf.columns.tolist()
    # print(dfCols)
    wbesRtmIexDf1=wbesRtmIexDf[['date_time','North-West \n- NR to WR - ','West-North \n- WR to NR - ','South-West \n- SR to WR - ','West-South \n- WR to SR - ', 'East-West \n- ER to WR - ', 'West-East \n- WR to ER - ']]
    wbesRtmIexDf.drop(['North-West \n- NR to WR - ','West-North \n- WR to NR - ','South-West \n- SR to WR - ','West-South \n- WR to SR - ', 'East-West \n- ER to WR - ', 'West-East \n- WR to ER - '], axis=1,inplace=True)

    wbesRtmIexDf1.loc[:, 'beneficiary_type'] = 'path'
    wbesRtmIexDf = pd.melt(wbesRtmIexDf, id_vars=['date_time'])
    wbesRtmIexDf1 = pd.melt(wbesRtmIexDf1, id_vars=['date_time','beneficiary_type'])
    wbesRtmIexDf1 = wbesRtmIexDf1.rename(columns={'variable': 'beneficiary'})
    wbesRtmIexDf1['beneficiary'] = wbesRtmIexDf1['beneficiary'].str.replace('\n','')


    wbesRtmIexDf[['beneficiary','Sec','d']]=wbesRtmIexDf['variable'].str.split('\n-',expand=True)
    wbesRtmIexDf[['beneficiary_type','c']]=wbesRtmIexDf['d'].str.split('-',expand=True)
    wbesRtmIexDf.drop(['Sec','variable','d','c'],axis=1,inplace=True)
    wbesRtmIexDf=wbesRtmIexDf.append(wbesRtmIexDf1, ignore_index = True)
    wbesRtmIexDf = wbesRtmIexDf.rename(columns={'value': 'data_val'})

    wbesRtmIexRecord = wbesRtmIexDf.to_dict('records')

    return wbesRtmIexRecord
