from src.config.appConfig import initConfig
from src.DataFetcher.statesHourlyDataFetcher import getStatesHourlyData
from src.DataFetcher.statesDailyDataFetcher import getStatesDailyData
from src.DataFetcher.linesGenDailyDataFetcher import getGenLinesDailyData
from src.config.appConfig import getFileMappings, getJsonConfig
import datetime as dt
from src.typeDefs.measRecord import IMetricsDataRecord
from typing import List

initConfig()
fileObjs = getFileMappings()
# getStatesHourlyData(fileObjs[0], dt.datetime(2021,1,1) )
# states daily data
# getStatesDailyData(fileObjs[1], dt.datetime(2021,1,1), 1 )
# gen line daily data
getGenLinesDailyData()

