from src.config.appConfig import getJsonConfig
# from src.dataFetchers.dataFetcherHandler import getIexGdamData
from src.dataFetchers.iexGdamDataFetcher import getIexGdamData
from src.repos.measDataRepo import MeasDataRepo
from typing import List
import datetime as dt


def iexGdamService(iexGdamFilePath):
    iexGdamRecords = getIexGdamData(iexGdamFilePath)
    measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

    isRawCreationSuccess = measDataRepo.insertIexGdamData(iexGdamRecords)
    if isRawCreationSuccess:
        print("IEX GDAM data insertion SUCCESSFUL")
    else:
        print("IEX GDAM data insertion UNSUCCESSFUL")
    return True
