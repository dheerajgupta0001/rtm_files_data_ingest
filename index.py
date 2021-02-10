from src.config.appConfig import initConfig
from src.DataFetcher.dataFetcher import getStatesHourlyData
from src.config.appConfig import getFileMappings
import datetime as dt
from datetime import timedelta

initConfig()

getStatesHourlyData(getFileMappings[0], dt.now() - timedelta(month=1) )

