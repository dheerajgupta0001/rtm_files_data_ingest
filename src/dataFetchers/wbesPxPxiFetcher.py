from typing import Dict
import pandas as pd
import datetime as dt
from src.typeDefs.wbesRtmPxiRecord import IWbesRtmPxiDataRecord
from typing import List
import csv
import numpy as np


def getWbesPxPxiData(targetFilePath: str, targetDt : dt.datetime) -> List[IWbesRtmPxiDataRecord]:
    wbesPxPxiRecord: List[IWbesRtmPxiDataRecord] = []
    wbesPxPxiDf = pd.read_excel(targetFilePath,skiprows=4, skipfooter=7)
    dfCols=wbesPxPxiDf.columns.tolist()
    # print(dfCols)
    wbesPxPxiDf['date_time'] = targetDt
    wbesPxPxiDf[['Hrs','Sec']]=wbesPxPxiDf['Time Desc'].str.split('-',expand=True)

    # print('The dataframe columns are {0}'.format(colNames))
    # wbesRtmIexDf['Date '] = pd.to_datetime(wbesRtmIexDf['Date '])
    wbesPxPxiDf['Hrs'] = pd.to_datetime(wbesPxPxiDf['Hrs']).dt.time
    new_ind = []
    tms = wbesPxPxiDf['Hrs']
    dates=wbesPxPxiDf['date_time']
    for x in range(0, len(dates)):
        n = dates[x]+dt.timedelta(hours=tms[x].hour, minutes=tms[x].minute)
        new_ind.append(n)

    wbesPxPxiDf['date_time'] = new_ind
    wbesPxPxiDf.drop(['Sec','Time Block','Hrs','Time Desc','Grand Total'],axis=1,inplace=True)

    dfCols=wbesPxPxiDf.columns.tolist()
    # print(dfCols)
    wbesPxPxiDf1=wbesPxPxiDf[['date_time','North-West \n- NR to WR - ','West-North \n- WR to NR - ','South-West \n- SR to WR - ','West-South \n- WR to SR - ', 'East-West \n- ER to WR - ', 'West-East \n- WR to ER - ']]
    wbesPxPxiDf.drop(['North-West \n- NR to WR - ','West-North \n- WR to NR - ','South-West \n- SR to WR - ','West-South \n- WR to SR - ', 'East-West \n- ER to WR - ', 'West-East \n- WR to ER - '], axis=1,inplace=True)

    wbesPxPxiDf1.loc[:, 'beneficiary_type'] = 'path'
    wbesPxPxiDf = pd.melt(wbesPxPxiDf, id_vars=['date_time'])
    wbesPxPxiDf1 = pd.melt(wbesPxPxiDf1, id_vars=['date_time','beneficiary_type'])
    wbesPxPxiDf1 = wbesPxPxiDf1.rename(columns={'variable': 'beneficiary'})
    wbesPxPxiDf1['beneficiary'] = wbesPxPxiDf1['beneficiary'].str.replace('\n','')

    wbesPxPxiDf[['beneficiary','Sec','d']]=wbesPxPxiDf['variable'].str.split('\n-',expand=True)
    wbesPxPxiDf[['beneficiary_type','c']]=wbesPxPxiDf['d'].str.split('-',expand=True)
    wbesPxPxiDf.drop(['Sec','variable','d','c'],axis=1,inplace=True)
    wbesPxPxiDf=wbesPxPxiDf.append(wbesPxPxiDf1, ignore_index = True)
    wbesPxPxiDf = wbesPxPxiDf.rename(columns={'value': 'data_val'})

    # print(wbesPxPxiDf1)

    wbesPxPxiRecord = wbesPxPxiDf.to_dict('records')

    return wbesPxPxiRecord

