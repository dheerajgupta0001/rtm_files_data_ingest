from typing import Dict
import pandas as pd
import datetime as dt
from src.typeDefs.freqVoltConfig import IFreqVoltConfig
from src.typeDefs.voltRecord import IVoltDataRecord
from typing import List


def getDailyVoltData(freqVoltConfigs: List[IFreqVoltConfig], targetFilePath: str) -> List[IVoltDataRecord]:
    voltRecords: List[IVoltDataRecord] = []

    vol_400_sht = ''
    vol_765_sht = ''
    # find the sheet that has freq data
    for c in freqVoltConfigs:
        if c["data_type"] == 'volt_400':
            vol_400_sht = c['sheet']
        elif c["data_type"] == 'volt_765':
            vol_765_sht = c['sheet']

    voltSheetsInfo = [
        {"lvl": 400, "sht": vol_400_sht},
        {"lvl": 765, "sht": vol_765_sht}
    ]

    for shtInfo in voltSheetsInfo:
        shtName = shtInfo['sht']
        volLvl = shtInfo['lvl']
        if not shtName == '':
            voltDf = pd.read_excel(
                targetFilePath, sheet_name=shtName, header=[0, 1])
            voltDf = pd.melt(voltDf, id_vars=[voltDf.columns[0]])
            voltDf = voltDf.rename(columns={
                voltDf.columns[0]: 'data_time', 'variable_0': 'entity_name', 'variable_1': 'metric_name', 'value': 'data_val'})
            voltDf['volt_level'] = volLvl
            voltRecords.extend(voltDf.to_dict('records'))

    for v in voltRecords:
        v['data_val'] = str(v['data_val'])

    return voltRecords
