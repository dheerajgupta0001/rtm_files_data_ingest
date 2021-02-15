from src.config.appConfig import initConfigs
from src.config.appConfig import getStateConfigs, getFileMappings
from src.app.statesHourlyService import statesHourlyService
from src.app.statesDailyService import statesDailyService
from src.app.freqDailyService import freqDailyService
from src.dataFetchers.dataFetcherHandler import getExcelFilePath
from src.app.linesGenService import linesGenService
from src.app.voltDailyService import voltDailyService
import datetime as dt

initConfigs()
filesSheet = getFileMappings()
statesConfigSheet = getStateConfigs()

targetMonth = dt.datetime(2021, 1, 1)


for eachrow in filesSheet:
    print(eachrow['file_type'])
    excelFilePath = getExcelFilePath(eachrow, targetMonth)
    if eachrow['file_type'] == 'state_hourly_data':
        statesHourlyService(statesConfigSheet , excelFilePath)
    if eachrow['file_type'] == 'state_daily_data':
        statesDailyService(statesConfigSheet , excelFilePath)
    if eachrow['file_type'] == 'gen_lines_daily_data':
        linesGenService(statesConfigSheet , excelFilePath)
    if eachrow['file_type'] == 'freq_vol_data':
        freqDailyService(excelFilePath)
        voltDailyService(excelFilePath)
