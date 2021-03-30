from src.config.appConfig import getJsonConfig
from src.dataFetchers.dataFetcherHandler import getWbesRtmIexData
from src.repos.measDataRepo import MeasDataRepo
from typing import List
import datetime as dt


def wbesRtmIexService(iexDamFilePath : str, targetDt: dt.datetime):
    wbesRtmIexRecords = getWbesRtmIexData(iexDamFilePath, targetDt)
    measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

    isRawCreationSuccess = measDataRepo.insertWbesRtmIexData(wbesRtmIexRecords)
    if isRawCreationSuccess:
        print("Wbes Rtm Iex Data insertion SUCCESSFUL")
    else:
        print("Wbes Rtm Iex Data insertion UNSUCCESSFUL")
    return True
