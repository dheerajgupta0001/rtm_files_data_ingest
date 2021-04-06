from typing import Dict
import pandas as pd
import datetime as dt
from src.typeDefs.wbesRtmPxiRecord import IWbesRtmPxiDataRecord
from typing import List
import csv
import numpy as np


def getWbesRtmPxiData(targetFilePath: str, targetDt : dt.datetime) -> List[IWbesRtmPxiDataRecord]:
    wbesRtmPxiRecord: List[IWbesRtmPxiDataRecord] = []
    wbesRtmPxiDf = pd.read_excel(targetFilePath,skiprows=4, skipfooter=6)
    dfCols=wbesRtmPxiDf.columns.tolist()
    # print(dfCols)
    wbesRtmPxiDf['date_time'] = targetDt
    wbesRtmPxiDf[['Hrs','Sec']]=wbesRtmPxiDf['Time Desc'].str.split('-',expand=True)

    # print('The dataframe columns are {0}'.format(colNames))
    # wbesRtmIexDf['Date '] = pd.to_datetime(wbesRtmIexDf['Date '])
    wbesRtmPxiDf['Hrs'] = pd.to_datetime(wbesRtmPxiDf['Hrs']).dt.time
    new_ind = []
    tms = wbesRtmPxiDf['Hrs']
    dates=wbesRtmPxiDf['date_time']
    for x in range(0, len(dates)):
        n = dates[x]+dt.timedelta(hours=tms[x].hour, minutes=tms[x].minute)
        new_ind.append(n)

    wbesRtmPxiDf['date_time'] = new_ind
    wbesRtmPxiDf.drop(['Sec','Time Block','Hrs','Time Desc','Grand Total'],axis=1,inplace=True)

    dfCols=wbesRtmPxiDf.columns.tolist()
    # print(dfCols)
    wbesRtmPxiDf1=wbesRtmPxiDf[['date_time','North-West \n- NR to WR - ','West-North \n- WR to NR - ','South-West \n- SR to WR - ','West-South \n- WR to SR - ', 'East-West \n- ER to WR - ', 'West-East \n- WR to ER - ']]
    wbesRtmPxiDf.drop(['North-West \n- NR to WR - ','West-North \n- WR to NR - ','South-West \n- SR to WR - ','West-South \n- WR to SR - ', 'East-West \n- ER to WR - ', 'West-East \n- WR to ER - '], axis=1,inplace=True)

    wbesRtmPxiDf1.loc[:, 'beneficiary_type'] = 'path'
    wbesRtmPxiDf = pd.melt(wbesRtmPxiDf, id_vars=['date_time'])
    wbesRtmPxiDf1 = pd.melt(wbesRtmPxiDf1, id_vars=['date_time','beneficiary_type'])
    wbesRtmPxiDf1 = wbesRtmPxiDf1.rename(columns={'variable': 'beneficiary'})
    wbesRtmPxiDf1['beneficiary'] = wbesRtmPxiDf1['beneficiary'].str.replace('\n','')

    wbesRtmPxiDf[['beneficiary','Sec','d']]=wbesRtmPxiDf['variable'].str.split('\n-',expand=True)
    wbesRtmPxiDf[['beneficiary_type','c']]=wbesRtmPxiDf['d'].str.split('-',expand=True)
    wbesRtmPxiDf.drop(['Sec','variable','d','c'],axis=1,inplace=True)
    wbesRtmPxiDf=wbesRtmPxiDf.append(wbesRtmPxiDf1, ignore_index = True)
    wbesRtmPxiDf = wbesRtmPxiDf.rename(columns={'value': 'data_val'})

    # print(wbesRtmPxiDf1)

    wbesRtmPxiRecord = wbesRtmPxiDf.to_dict('records')

    return wbesRtmPxiRecord

