from src.config.appConfig import initConfigs
from src.config.appConfig import getStateConfigs,getFileMappings
from src.app.statesHourlyService import statesHourlyService
from src.app.statesDailyService import statesDailyService
from src.dataFetchers.dataFetcher import getExcelFilePath
import datetime as dt

initConfigs()
filesSheet = getFileMappings()
statesConfigSheet = getStateConfigs()

targetMonth = dt.datetime(2021,1,1) 

# derive file path for hourly, then call service

# derive file path for daily

for eachrow in filesSheet:
    print(eachrow['file_type'])
    excelFilePath = getExcelFilePath(eachrow , targetMonth )
    if eachrow['file_type'] == 'state_hourly_data':
        pass
        # statesHourlyService(statesConfigSheet , excelFilePath)

    elif eachrow['file_type'] == 'state_daily_data':
        statesDailyService(statesConfigSheet , excelFilePath)