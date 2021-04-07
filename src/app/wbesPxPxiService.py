from src.config.appConfig import getJsonConfig
from src.dataFetchers.dataFetcherHandler import getWbesPxPxiData
from src.repos.measDataRepo import MeasDataRepo
from typing import List
import datetime as dt


def wbesPxPxiService(pxPxiFilePath : str, targetDt: dt.datetime):
    wbesPxPxiRecords = getWbesPxPxiData(pxPxiFilePath, targetDt)
    measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

    isRawCreationSuccess = measDataRepo.insertWbesPxPxiData(wbesPxPxiRecords)
    if isRawCreationSuccess:
        print("Wbes Px Pxi Data insertion SUCCESSFUL")
    else:
        print("Wbes Px Pxi Data insertion UNSUCCESSFUL")
    return True
