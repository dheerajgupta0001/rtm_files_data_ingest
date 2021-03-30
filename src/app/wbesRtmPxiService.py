from src.config.appConfig import getJsonConfig
from src.dataFetchers.dataFetcherHandler import getWbesRtmPxiData
from src.repos.measDataRepo import MeasDataRepo
from typing import List
import datetime as dt


def wbesRtmPxiService(iexDamFilePath : str, targetDt: dt.datetime):
    wbesRtmIexRecords = getWbesRtmPxiData(iexDamFilePath, targetDt)
    measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

    isRawCreationSuccess = measDataRepo.insertWbesRtmPxiData(wbesRtmIexRecords)
    if isRawCreationSuccess:
        print("Wbes Rtm Pxi data insertion SUCCESSFUL")
    else:
        print("Wbes Rtm Pxi data insertion UNSUCCESSFUL")
    return True
