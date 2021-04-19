from src.config.appConfig import getJsonConfig
from src.dataFetchers.dataFetcherHandler import getIexGtamData
from src.repos.measDataRepo import MeasDataRepo
from typing import List
import datetime as dt


def iexGtamService(iexGtamFilePath):
    iexGtamRecords, iexGtamTableRecords = getIexGtamData(iexGtamFilePath)
    measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

    isRawCreationSuccess = measDataRepo.insertIexGtamData(iexGtamRecords)
    isderivedCreationSuccess = measDataRepo.insertIexGtamDeriveData(iexGtamTableRecords)

    if isRawCreationSuccess:
        print("IEX GTAM raw data insertion SUCCESSFUL")
    else:
        print("IEX GTAM raw data insertion UNSUCCESSFUL")

    if isderivedCreationSuccess:
        print("IEX GTAM derived data insertion SUCCESSFUL")
    else:
        print("IEX GTAM derived data insertion UNSUCCESSFUL")
    return True
