from typing import Dict
import pandas as pd
import datetime as dt
from src.typeDefs.freqVoltConfig import IFreqVoltConfig
from src.typeDefs.freqRecord import IFreqDataRecord
from typing import List


def getFreqData(freqVoltConfigs: List[IFreqVoltConfig], targetFilePath: str) -> List[IFreqDataRecord]:
    freqRecords: List[IFreqDataRecord] = []

    freqSheet = ''
    # find the sheet that has freq data
    for c in freqVoltConfigs:
        if c["data_type"] == 'freq':
            freqSheet = c['sheet']

    if freqSheet == '':
        return []

    freqDf = pd.read_excel(
        targetFilePath, sheet_name=freqSheet)
    freqDf = pd.melt(freqDf, id_vars=['Date'])
    freqDf = freqDf.rename(columns={
        'variable': 'metric_name', 'value': 'data_val',
        'Date': 'data_time'})
    freqRecords = freqDf.to_dict('records')

    for f in freqRecords:
        f['data_val'] = str(f['data_val'])

    return freqRecords
