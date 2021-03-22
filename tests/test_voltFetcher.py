import unittest
from src.dataFetchers.voltageDailyFetcher import getDailyVoltData
from src.config.appConfig import loadFreqVoltConfigs, loadFileMappings
from src.dataFetchers.dataFetcherHandler import getExcelFilePath
import datetime as dt


class TestFreqDataFetcher(unittest.TestCase):
    def test_voltDailyDataFetch(self) -> None:
        """tests the function that tests file mappings config
        """
        freqVoltConfigs = loadFreqVoltConfigs()
        fMappings = loadFileMappings()
        volFileMapping = {}
        for f in fMappings:
            if f['file_type'] == 'freq_vol_data':
                volFileMapping = f
        targetMonth = dt.datetime(2021, 1, 1)
        voltFilePath = getExcelFilePath(volFileMapping, targetMonth)
        voltRecords = getDailyVoltData(freqVoltConfigs, voltFilePath)
        print(voltRecords)
        self.assertTrue(voltRecords is not None)
        self.assertFalse(len(voltRecords) == 0)
