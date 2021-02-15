from src.config.appConfig import getFreqVoltConfigs, getJsonConfig
from src.dataFetchers.voltageDailyFetcher import getDailyVoltData
from src.repos.measData.measDataRepo import MeasDataRepo
from typing import List
import datetime as dt


def voltDailyService(voltFilePath):
    freqVoltConfigs = getFreqVoltConfigs()
    voltRecords = getDailyVoltData(freqVoltConfigs, voltFilePath)
    measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

    isRawCreationSuccess = measDataRepo.insertDaywiseVoltMetrics(voltRecords)
    if isRawCreationSuccess:
        print("Volt Daily data insertion SUCCESSFUL")
    else:
        print("Volt Daily data insertion UNSUCCESSFUL")
