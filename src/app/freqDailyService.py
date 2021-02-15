from src.config.appConfig import getFreqVoltConfigs, getJsonConfig
from src.dataFetchers.dataFetcherHandler import getFreqData
from src.typeDefs.stateConfig import IStateConfig
from src.repos.measData.measDataRepo import MeasDataRepo
from typing import List
import datetime as dt


def freqDailyService(freqFilePath):
    freqVoltConfigs = getFreqVoltConfigs()
    freqRecords = getFreqData(freqVoltConfigs, freqFilePath)
    measDataRepo = MeasDataRepo(getJsonConfig()['appDbConnStr'])

    isRawCreationSuccess = measDataRepo.insertDaywiseFreqMetrics(freqRecords)
    if isRawCreationSuccess:
        print("Freq Daily data insertion SUCCESSFUL")
    else:
        print("Freq Daily data insertion UNSUCCESSFUL")
