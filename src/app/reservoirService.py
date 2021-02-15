from src.config.appConfig import getJsonConfig
from src.dataFetchers.dataFetcherHandler import reservoirDataFetcherHandler
from src.typeDefs.stateConfig import IStateConfig
from src.repos.measData.measDataRepo import MeasDataRepo
from typing import List

def reservoirService(excelFilePath):
    reservoirRecords = reservoirDataFetcherHandler(excelFilePath)
    measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

    isRawCreationSuccess = False
    # print(each)
    
    isRawCreationSuccess = measDataRepo.insertReservoirDailyData(reservoirRecords)

    if isRawCreationSuccess:
        print("Reservoir data insertion SUCCESSFUL")
    else:
        print("Reservoir data insertion UNSUCCESSFUL")


    