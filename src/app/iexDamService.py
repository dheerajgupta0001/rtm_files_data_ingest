from src.config.appConfig import getJsonConfig
from src.dataFetchers.dataFetcherHandler import getIexDamData
from src.repos.measDataRepo import MeasDataRepo
from typing import List
import datetime as dt


def iexDamService(iexDamFilePath):
    iexDamRecords = getIexDamData(iexDamFilePath)
    measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

    isRawCreationSuccess = measDataRepo.insertIexDamData(iexDamRecords)
    if isRawCreationSuccess:
        print("IEX DAM data insertion SUCCESSFUL")
    else:
        print("IEX DAM data insertion UNSUCCESSFUL")
    return True
