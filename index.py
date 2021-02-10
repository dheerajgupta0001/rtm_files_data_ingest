from src.config.appConfig import initConfig
from src.DataFetcher.statesHourlyDataFetcher import getStatesHourlyData
from src.config.appConfig import getFileMappings
import datetime as dt

initConfig()
fileObjs = getFileMappings()
getStatesHourlyData(fileObjs[0], dt.datetime(2021,1,1) )

