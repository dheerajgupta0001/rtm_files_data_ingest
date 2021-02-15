from src.config.appConfig import getJsonConfig
from src.dataFetchers.dataFetcherHandler import linesGenDataFetcherHandler
from src.typeDefs.stateConfig import IStateConfig
from src.repos.measData.measDataRepo import MeasDataRepo
from typing import List

def linesGenService(stateConfigSheet :List[IStateConfig], excelFilePath):
    linesGenRecords = linesGenDataFetcherHandler(stateConfigSheet, excelFilePath)
    measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

    for each in linesGenRecords:
        isRawCreationSuccess = False
        # print(each)
        
        isRawCreationSuccess = measDataRepo.insertGenLinesDailyData(each)

        if isRawCreationSuccess:
            print("State Daily data insertion SUCCESSFUL for {0}".format(each[0]['entity_tag']))
        else:
            print("State Daily data insertion UNSUCCESSFUL for {0}".format(each[0]['entity_tag']))


    