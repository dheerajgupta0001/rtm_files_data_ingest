from src.config.appConfig import initConfigs
from src.config.appConfig import getFileMappings, getJsonConfig , getStateConfigs
from src.dataFetchers.dataFetcherHandler import statesDailyDataFetcherHandler
from src.typeDefs.stateConfig import IStateConfig
from src.repos.measData.measDataRepo import MeasDataRepo
from typing import List

initConfigs()
filesSheet = getFileMappings()
stateConfigSheet = getStateConfigs()

def statesDailyService(stateConfigSheet :List[IStateConfig], excelFilePath):
    stateDailyRecords = statesDailyDataFetcherHandler(stateConfigSheet, excelFilePath)
    measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

    for each in stateDailyRecords:
        isRawCreationSuccess = False
        # print(each)
        
        isRawCreationSuccess = measDataRepo.insertStatesDailyData(each)

        if isRawCreationSuccess:
            print("State Daily data insertion SUCCESSFUL for {0}".format(each[0]['entity_tag']))
        else:
            print("State Daily data insertion UNSUCCESSFUL for {0}".format(each[0]['entity_tag']))


