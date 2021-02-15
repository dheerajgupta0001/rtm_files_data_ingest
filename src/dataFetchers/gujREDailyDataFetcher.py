from typing import Dict
import pandas as pd
import datetime as dt
from datetime import timedelta
from src.typeDefs.stateConfig import IStateConfig
from src.typeDefs.measRecord import IMetricsDataRecord
from typing import List, Any


def getGujREGenerationData(targetFilePath: str) -> List[List[IMetricsDataRecord]]:
    
    allGujRERecords:List[List[IMetricsDataRecord]] = []
    gujREGenerationDailyRecords: List[IMetricsDataRecord] = []
    
    excelWorkBook = pd.ExcelFile(targetFilePath)
    gujREGenerationSheets = excelWorkBook.sheet_names

    for eachDaySheet in gujREGenerationSheets:
        df = pd.read_excel(targetFilePath, sheet_name=eachDaySheet, nrows=1, header=None)
        dateCells = [x for x in df.iloc[0,:] if isinstance(x, dt.datetime)]
        if len(dateCells) == 0:
            continue
        dataSheetDf = pd.read_excel(targetFilePath , sheet_name=eachDaySheet ,skiprows=1)
        if dataSheetDf.shape[0] > 24:
            dataSheetDf = dataSheetDf.iloc[0:24, :]
        newCols = [x for x in dataSheetDf.columns if not (x.startswith('Unnamed') or x.isspace())]
        dataSheetDf = dataSheetDf[newCols]
        dataSheetDf['Date'] = dateCells[0]
        dataSheetDf['Date'] += pd.to_timedelta(dataSheetDf.Hours, unit='h')
        del dataSheetDf['Hours']
        dataSheetDf.columns = [' '.join(x.split()) for x in dataSheetDf.columns]
        dataSheetDf = pd.melt(dataSheetDf, id_vars=['Date'])
        dataSheetDf['entity_tag'] = 'gujrat'
        dataSheeetDf = dataSheetDf.rename(columns={
                    dataSheetDf.columns[0]: 'data_time', 'variable': 'metric_name',
                    'value': 'data_val'})


        gujREGenerationDailyRecords = dataSheeetDf.to_dict('records')

        allGujRERecords.append(gujREGenerationDailyRecords)
        
    return allGujRERecords

