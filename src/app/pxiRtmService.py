from src.config.appConfig import getJsonConfig
from src.dataFetchers.dataFetcherHandler import getPxiRtmData
from src.repos.measDataRepo import MeasDataRepo
from typing import List
import datetime as dt


def pxiRtmService(pxiRtmFilePath):
    pxiRtmRecords = getPxiRtmData(pxiRtmFilePath)
    measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

    isRawCreationSuccess = measDataRepo.insertPxiRtmData(pxiRtmRecords)
    if isRawCreationSuccess:
        print("Pxi Rtm data insertion SUCCESSFUL")
    else:
        print("Pxi Rtm data insertion UNSUCCESSFUL")
    return True
