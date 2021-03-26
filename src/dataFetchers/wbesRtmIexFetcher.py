from typing import Dict
import pandas as pd
import datetime as dt
from src.typeDefs.wbesRtmIexRecord import IWbesRtmIexDataRecord
from typing import List
import csv
import numpy as np


def getWbesRtmIexData(targetFilePath: str, targetDt : dt.datetime) -> List[IWbesRtmIexDataRecord]:
    wbesRtmIexRecord: List[IWbesRtmIexDataRecord] = []

    with open(targetFilePath, mode='r') as f:
        # read all the file content   
        fLines = f.read()
        fLines = fLines.replace('\x00','').replace('\n\n', '\n').split('\n')
        # read header from first line
        dfCols = fLines[0].split(',')[2:-1]
        time_block = []

        schDfRows = []
        # read the values from line 1 to 100
        for rowInd in range(1,97):
            # read the data line
            dataRowVals = fLines[rowInd].split(',')
            block = [k for k in dataRowVals[1:-150]]
            time_block.append(block[0])
            dataRowVals = [float(k) for k in dataRowVals[2:-1]]
            schDfRows.append(dataRowVals)
        wbesRtmIexDf = pd.DataFrame(data=schDfRows, columns=dfCols)
        wbesRtmIexDf['time_block'] = time_block
        targetDt = targetDt.strftime("%d-%m-%Y")
        wbesRtmIexDf['date_time'] = str(targetDt)

        wbesRtmIexDf[['first_block','last_block']] = wbesRtmIexDf.time_block.str.split("-",expand=True)
        wbesRtmIexDf[['hour','minute']] = wbesRtmIexDf.first_block.str.split(":",expand=True)
        wbesRtmIexDf[['day','month','year']] = wbesRtmIexDf.date_time.str.split("-",expand=True)
        wbesRtmIexDf['date_time'] = pd.to_datetime(wbesRtmIexDf[['year', 'month', 'day', 'hour', 'minute']])
        wbesRtmIexDf = wbesRtmIexDf.drop(['year', 'month', 'day', 'first_block',
                                'last_block', 'hour','minute','Grand Total', 'time_block'], axis=1)
        # print(wbesRtmIexDf)
        wbesRtmIexDf1=wbesRtmIexDf[['date_time','North-West | - NR to WR - ','West-North | - WR to NR - ','South-West | - SR to WR - ','West-South | - WR to SR - ', 'East-West | - ER to WR - ', 'West-East | - WR to ER - ']]
        wbesRtmIexDf.drop(['North-West | - NR to WR - ', 'West-North | - WR to NR - ', 'South-West | - SR to WR - ','West-South | - WR to SR - ', 'East-West | - ER to WR - ', 'West-East | - WR to ER - '], axis=1,inplace=True)

        wbesRtmIexDf1.loc[:,'beneficiary_type']='path'
        wbesRtmIexDf = pd.melt(wbesRtmIexDf, id_vars=['date_time'])
        wbesRtmIexDf1 = pd.melt(wbesRtmIexDf1, id_vars=['date_time','beneficiary_type'])
        wbesRtmIexDf1 = wbesRtmIexDf1.rename(columns={'variable': 'beneficiary'})

        wbesRtmIexDf[['beneficiary','Sec','d']]=wbesRtmIexDf['variable'].str.split('|',expand=True)
        wbesRtmIexDf[['a','beneficiary_type','c']]=wbesRtmIexDf['d'].str.split('-',expand=True)
        wbesRtmIexDf.drop(['Sec','variable','d','a','c'],axis=1,inplace=True)
        wbesRtmIexDf=wbesRtmIexDf.append(wbesRtmIexDf1, ignore_index = True)
        wbesRtmIexDf = wbesRtmIexDf.rename(columns={'value': 'data_val'})



    wbesRtmIexRecord = wbesRtmIexDf.to_dict('records')

    return wbesRtmIexRecord
