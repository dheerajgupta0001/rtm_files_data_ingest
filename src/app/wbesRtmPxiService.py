from src.config.appConfig import getJsonConfig
from src.dataFetchers.dataFetcherHandler import getWbesRtmPxiData
# from src.repos.measData.measDataRepo import MeasDataRepo
from typing import List
import datetime as dt


def wbesRtmPxiService(iexDamFilePath : str, targetDt: dt.datetime):
    wbesRtmIexRecords = getWbesRtmPxiData(iexDamFilePath, targetDt)
    # measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

    # isRawCreationSuccess = measDataRepo.insertDaywiseFreqMetrics(wbesRtmIexRecords)
    # if isRawCreationSuccess:
    #     print("Freq Daily data insertion SUCCESSFUL")
    # else:
    #     print("Freq Daily data insertion UNSUCCESSFUL")
    return True
