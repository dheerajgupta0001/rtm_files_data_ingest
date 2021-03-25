from src.config.appConfig import getJsonConfig
from src.dataFetchers.dataFetcherHandler import getIexGtamData
from src.repos.measDataRepo import MeasDataRepo
from typing import List
import datetime as dt


def iexGtamService(iexGtamFilePath):
    iexGtamRecords = getIexGtamData(iexGtamFilePath)
    measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

    isRawCreationSuccess = measDataRepo.insertIexGtamData(iexGtamRecords)
    if isRawCreationSuccess:
        print("IEX GTAM data insertion SUCCESSFUL")
    else:
        print("IEX GTAM data insertion UNSUCCESSFUL")
    return True
