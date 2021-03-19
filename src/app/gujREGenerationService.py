from src.config.appConfig import getJsonConfig
from src.dataFetchers.dataFetcherHandler import gujREGenerationDataFetcherHandler
from src.repos.measData.measDataRepo import MeasDataRepo
from typing import List

def gujREGenerationService(excelFilePath):
    gujREGenerationRecords = gujREGenerationDataFetcherHandler(excelFilePath)
    measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

    for each in gujREGenerationRecords:
        
        isRawCreationSuccess = measDataRepo.insertStatesHourlyData(each)

        if isRawCreationSuccess:
            print("Guj RE Daily data insertion SUCCESSFUL on {0}".format(each[0]['data_time']))
        else:
            print("Guj RE Daily data insertion UNSUCCESSFUL on {0}".format(each[0]['data_time']))


    