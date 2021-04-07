from src.config.appConfig import getJsonConfig
from src.dataFetchers.dataFetcherHandler import getWbesPxIexData
from src.repos.measDataRepo import MeasDataRepo
from typing import List
import datetime as dt


def wbesPxIexService(pxIexFilePath : str, targetDt: dt.datetime):
    wbesPxIexRecords = getWbesPxIexData(pxIexFilePath, targetDt)
    measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

    isRawCreationSuccess = measDataRepo.insertWbesPxIexData(wbesPxIexRecords)
    if isRawCreationSuccess:
        print("Wbes Px Iex Data insertion SUCCESSFUL")
    else:
        print("Wbes Px Iex Data insertion UNSUCCESSFUL")
    return True
