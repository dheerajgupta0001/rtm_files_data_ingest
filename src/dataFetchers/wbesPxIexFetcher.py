from typing import Dict
import pandas as pd
import datetime as dt
from src.typeDefs.wbesRtmIexRecord import IWbesRtmIexDataRecord
from typing import List
import csv
import numpy as np


def getWbesPxIexData(targetFilePath: str, targetDt : dt.datetime) -> List[IWbesRtmIexDataRecord]:
    wbesPxIexRecord: List[IWbesRtmIexDataRecord] = []

    wbesPxIexDf = pd.read_excel(targetFilePath,skiprows=4, skipfooter=7)
    dfCols=wbesPxIexDf.columns.tolist()
    # print(dfCols)
    wbesPxIexDf['date_time'] = targetDt
    wbesPxIexDf[['Hrs','Sec']]=wbesPxIexDf['Time Desc'].str.split('-',expand=True)

    # print('The dataframe columns are {0}'.format(colNames))
    # wbesPxIexDf['Date '] = pd.to_datetime(wbesPxIexDf['Date '])
    wbesPxIexDf['Hrs'] = pd.to_datetime(wbesPxIexDf['Hrs']).dt.time
    new_ind = []
    tms = wbesPxIexDf['Hrs']
    dates=wbesPxIexDf['date_time']
    for x in range(0, len(dates)):
        n = dates[x]+dt.timedelta(hours=tms[x].hour, minutes=tms[x].minute)
        new_ind.append(n)

    wbesPxIexDf['date_time'] = new_ind
    wbesPxIexDf.drop(['Sec','Time Block','Hrs','Time Desc','Grand Total'],axis=1,inplace=True)

    dfCols=wbesPxIexDf.columns.tolist()
    # print(dfCols)
    wbesPxIexDf1=wbesPxIexDf[['date_time','North-West \n- NR to WR - ','West-North \n- WR to NR - ','South-West \n- SR to WR - ','West-South \n- WR to SR - ', 'East-West \n- ER to WR - ', 'West-East \n- WR to ER - ']]
    wbesPxIexDf.drop(['North-West \n- NR to WR - ','West-North \n- WR to NR - ','South-West \n- SR to WR - ','West-South \n- WR to SR - ', 'East-West \n- ER to WR - ', 'West-East \n- WR to ER - '], axis=1,inplace=True)

    wbesPxIexDf1.loc[:, 'beneficiary_type'] = 'path'
    wbesPxIexDf = pd.melt(wbesPxIexDf, id_vars=['date_time'])
    wbesPxIexDf1 = pd.melt(wbesPxIexDf1, id_vars=['date_time','beneficiary_type'])
    wbesPxIexDf1 = wbesPxIexDf1.rename(columns={'variable': 'beneficiary'})
    wbesPxIexDf1['beneficiary'] = wbesPxIexDf1['beneficiary'].str.replace('\n','')


    wbesPxIexDf[['beneficiary','Sec','d']]=wbesPxIexDf['variable'].str.split('\n-',expand=True)
    wbesPxIexDf[['beneficiary_type','c']]=wbesPxIexDf['d'].str.split('-',expand=True)
    wbesPxIexDf.drop(['Sec','variable','d','c'],axis=1,inplace=True)
    wbesPxIexDf=wbesPxIexDf.append(wbesPxIexDf1, ignore_index = True)
    wbesPxIexDf = wbesPxIexDf.rename(columns={'value': 'data_val'})

    wbesPxIexRecord = wbesPxIexDf.to_dict('records')

    return wbesPxIexRecord
