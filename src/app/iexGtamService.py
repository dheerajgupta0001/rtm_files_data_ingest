from src.config.appConfig import getJsonConfig
from src.dataFetchers.dataFetcherHandler import getIexGtamData
from src.repos.measDataRepo import MeasDataRepo
from typing import List
import datetime as dt


def iexGtamService(iexGtamFilePath):
    iexGtamRecords, iexGtamTableRecords = getIexGtamData(iexGtamFilePath)
    measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

    isRawCreationSuccess = measDataRepo.insertIexGtamData(iexGtamRecords)
    isRawCreationSuccess1 = measDataRepo.insertIexGtamDeriveData(iexGtamTableRecords)

    if isRawCreationSuccess and isRawCreationSuccess1:
        print("IEX GTAM data insertion SUCCESSFUL")
    else:
        print("IEX GTAM data insertion UNSUCCESSFUL")
    return True
