from src.config.appConfig import getJsonConfig
from src.dataFetchers.dataFetcherHandler import getPxiDamData
from src.repos.measDataRepo import MeasDataRepo
from typing import List
import datetime as dt


def pxiDamService(pxiDamFilePath):
    pxiDamRecords = getPxiDamData(pxiDamFilePath)
    measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

    isRawCreationSuccess = measDataRepo.insertPxiDamData(pxiDamRecords)
    if isRawCreationSuccess:
        print("PXI DAM data insertion SUCCESSFUL")
    else:
        print("PXI DAM data insertion UNSUCCESSFUL")
    return True
