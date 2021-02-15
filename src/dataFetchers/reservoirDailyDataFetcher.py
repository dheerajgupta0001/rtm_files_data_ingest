from typing import Dict
import pandas as pd
import datetime as dt
from src.typeDefs.stateConfig import IStateConfig
from src.typeDefs.reservoirMeasRecord import IReservoirDataRecord
from typing import List, Any


def getReservoirDailyData(targetFilePath: str) -> List[List]:
    
    reservoirDailyRecords: List[IReservoirDataRecord] = []
   
    dataSheeetDf = pd.read_excel(targetFilePath, sheet_name='SSP Gen 2020-21', header=[0,1], skipfooter=365)
    # remove 1st column from df
    dataSheeetDf = dataSheeetDf.iloc[:, 1:]
    # dataSheeetDf.columns = ['_'.join(x) for x in dataSheeetDf.columns]
    dataSheeetDf = pd.melt(dataSheeetDf, id_vars=[dataSheeetDf.columns[0]])
    dataSheeetDf = dataSheeetDf.rename(columns={
                    dataSheeetDf.columns[0]: 'data_time', 'variable_0': 'entity_tag',
                    'variable_1': 'metric_tag','value': 'data_val'})
    # dataSheeetDf['entity_tag'] = eachRow['name']
    dataSheeetDf['data_val'].fillna(0, inplace=True)
    
    # convert dataframe to list of dictionaries
    reservoirDailyRecords = dataSheeetDf.to_dict('records')

        
    return reservoirDailyRecords
