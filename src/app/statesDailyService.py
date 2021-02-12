from src.config.appConfig import initConfigs
from src.dataFetchers.statesDailyDataFetcher import getStatesDailyData
from src.config.appConfig import getFileMappings, getJsonConfig , getStateConfigs
from src.dataFetchers.dataFetcher import statesDailyDataFetcher #right
from src.typeDefs.stateConfig import IStateConfig
from src.repos.measData.measDataRepo import MeasDataRepo
import datetime as dt
from typing import List

initConfigs()
filesSheet = getFileMappings()
stateConfigSheet = getStateConfigs()

def statesDailyService(stateConfigSheet :List[IStateConfig], excelFilePath):
    stateDailyRecords = statesDailyDataFetcher(stateConfigSheet, excelFilePath)
    measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

    for each in stateDailyRecords:
        isRawCreationSuccess = False
        # print(each)
        
        isRawCreationSuccess = measDataRepo.insertStatesHorlyData(each)

        if isRawCreationSuccess:
            print("State Daily data insertion SUCCESSFUL for {0}".format(each[0]['entity_tag']))
        else:
            print("State Daily data insertion UNSUCCESSFUL for {0}".format(each[0]['entity_tag']))


