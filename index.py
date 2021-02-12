from src.config.appConfig import initConfigs
# from src.DataFetcher.statesHourlyDataFetcher import getStatesHourlyData
from src.dataFetchers.dataFetcher import getExcelFilePath
from src.dataFetchers.statesHourlyDataFetcher import getStatesHourlyData
# from src.DataFetcher.statesDailyDataFetcher import getStatesDailyData
# from src.DataFetcher.linesGenDailyDataFetcher import getGenLinesDailyData
from src.config.appConfig import getFileMappings, getJsonConfig , getStateConfigs
from src.dataFetchers.dataFetcher import statesHourlyDataFetcher
from src.repos.measData.measDataRepo import MeasDataRepo
import datetime as dt
from typing import List

initConfigs()
filesSheet = getFileMappings()
stateConfigSheet = getStateConfigs()

#for current we are calling filesSheet[0] to get sfirst entry later we will use a loop for each file

stateHourlyRecords = statesHourlyDataFetcher(stateConfigSheet ,getExcelFilePath(filesSheet[0] ,dt.datetime(2021,1,1) ) )
# get the instance of state Hourly metrics data storage repository
measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

for each in stateHourlyRecords:
    isRawCreationSuccess = False
    print(each)
    break
    isRawCreationSuccess = measDataRepo.insertStatesHorlyData(each)
    if isRawCreationSuccess:
        print("State Hourly data insertion SUCCESSFUL for")
    else:
        print("State Hourly data insertion UNSUCCESSFUL for")

