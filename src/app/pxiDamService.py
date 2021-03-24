from src.config.appConfig import getJsonConfig
from src.dataFetchers.dataFetcherHandler import getPxiDamData
# from src.repos.measData.measDataRepo import MeasDataRepo
from typing import List
import datetime as dt


def pxiDamService(pxiDamFilePath):
    pxiDamRecords = getPxiDamData(pxiDamFilePath)
    # measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

    # isRawCreationSuccess = measDataRepo.insertDaywiseFreqMetrics(iexDamRecords)
    # if isRawCreationSuccess:
    #     print("Freq Daily data insertion SUCCESSFUL")
    # else:
    #     print("Freq Daily data insertion UNSUCCESSFUL")
    return True
