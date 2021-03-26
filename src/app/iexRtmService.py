from src.config.appConfig import getJsonConfig
from src.dataFetchers.dataFetcherHandler import getIexRtmData
from src.repos.measDataRepo import MeasDataRepo
from typing import List
import datetime as dt


def iexRtmService(iexRtmFilePath):
    iexRtmRecords = getIexRtmData(iexRtmFilePath)
    measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

    isRawCreationSuccess = measDataRepo.insertIexRtmData(iexRtmRecords)
    if isRawCreationSuccess:
        print("IEX RTM data insertion SUCCESSFUL")
    else:
        print("IEX RTM data insertion UNSUCCESSFUL")
    return True
