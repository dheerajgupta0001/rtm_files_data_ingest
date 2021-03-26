from typing import Dict
import pandas as pd
import datetime as dt
from src.typeDefs.wbesRtmPxiRecord import IWbesRtmPxiDataRecord
from typing import List
import csv
import numpy as np


def getWbesRtmPxiData(targetFilePath: str, targetDt : dt.datetime) -> List[IWbesRtmPxiDataRecord]:
    wbesRtmPxiRecord: List[IWbesRtmPxiDataRecord] = []
    with open(targetFilePath, mode='r') as f:
        # read all the file content
        fLines = f.read()
        fLines = fLines.replace('\x00', '').replace('\n\n', '\n').split('\n')
        # read header from first line
        dfCols = fLines[0].split(',')[2:-1]
        time_block = []

        schDfRows = []
        # read the values from line 1 to 100
        for rowInd in range(1, 97):
            # read the data line
            dataRowVals = fLines[rowInd].split(',')
            block = [k for k in dataRowVals[1:-150]]
            time_block.append(block[0])
            dataRowVals = [float(k) for k in dataRowVals[2:-1]]
            schDfRows.append(dataRowVals)
        wbesRtmPxiDf = pd.DataFrame(data=schDfRows, columns=dfCols)
        wbesRtmPxiDf['time_block'] = time_block
        targetDt = targetDt.strftime("%d-%m-%Y")
        wbesRtmPxiDf['date_time'] = str(targetDt)

        wbesRtmPxiDf[['first_block', 'last_block']] = wbesRtmPxiDf.time_block.str.split("-", expand=True)
        wbesRtmPxiDf[['hour', 'minute']] = wbesRtmPxiDf.first_block.str.split(":", expand=True)
        wbesRtmPxiDf[['day', 'month', 'year']] = wbesRtmPxiDf.date_time.str.split("-", expand=True)
        wbesRtmPxiDf['date_time'] = pd.to_datetime(wbesRtmPxiDf[['year', 'month', 'day', 'hour', 'minute']])
        wbesRtmPxiDf = wbesRtmPxiDf.drop(['year', 'month', 'day', 'first_block',
                                      'last_block', 'hour', 'minute', 'Grand Total', 'time_block'], axis=1)
        
        wbesRtmPxiDf1=wbesRtmPxiDf[['date_time','North-West | - NR to WR - ','West-North | - WR to NR - ','South-West | - SR to WR - ','West-South | - WR to SR - ', 'East-West | - ER to WR - ', 'West-East | - WR to ER - ']]

        wbesRtmPxiDf.drop(['North-West | - NR to WR - ','West-North | - WR to NR - ','South-West | - SR to WR - ','West-South | - WR to SR - ', 'East-West | - ER to WR - ', 'West-East | - WR to ER - '], axis=1, inplace=True)

        wbesRtmPxiDf1.loc[:,'beneficiary_type']='path'
        wbesRtmPxiDf = pd.melt(wbesRtmPxiDf, id_vars=['date_time'])
        wbesRtmPxiDf1 = pd.melt(wbesRtmPxiDf1, id_vars=['date_time','beneficiary_type'])
        wbesRtmPxiDf1 = wbesRtmPxiDf1.rename(columns={'variable': 'beneficiary'})

        wbesRtmPxiDf[['beneficiary','Sec','d']]=wbesRtmPxiDf['variable'].str.split('|',expand=True)
        wbesRtmPxiDf[['a','beneficiary_type','c']]=wbesRtmPxiDf['d'].str.split('-',expand=True)
        wbesRtmPxiDf.drop(['Sec','variable','d','a','c'],axis=1,inplace=True)
        wbesRtmPxiDf=wbesRtmPxiDf.append(wbesRtmPxiDf1, ignore_index = True)
        wbesRtmPxiDf = wbesRtmPxiDf1.rename(columns={'value': 'data_val'})
        # dfCols=wbesRtmPxiDf.columns.tolist()
        # print(dfCols)
    wbesRtmPxiRecord = wbesRtmPxiDf.to_dict('records')

    return wbesRtmPxiRecord

