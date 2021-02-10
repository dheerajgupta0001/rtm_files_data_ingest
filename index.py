from src.config.appConfig import initConfig
from src.DataFetcher.statesHourlyDataFetcher import getStatesHourlyData
from src.config.appConfig import getFileMappings, getJsonConfig
import datetime as dt
from src.typeDefs.measRecord import IMetricsDataRecord
from typing import List

initConfig()
fileObjs = getFileMappings()
stateHourlyRecords:List[IMetricsDataRecord] = getStatesHourlyData(fileObjs[0], dt.datetime(2021,1,1) )


