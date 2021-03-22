import unittest
from src.dataFetchers.freqDataFetcher import getFreqData
from src.config.appConfig import loadFreqVoltConfigs, loadFileMappings
from src.dataFetchers.dataFetcherHandler import getExcelFilePath
import datetime as dt


class TestFreqDataFetcher(unittest.TestCase):
    def test_freqDailyDataFetch(self) -> None:
        """tests the function that tests file mappings config
        """
        freqVoltConfigs = loadFreqVoltConfigs()
        fMappings = loadFileMappings()
        freqFileMapping = {}
        for f in fMappings:
            if f['file_type'] == 'freq_vol_data':
                freqFileMapping = f
        targetMonth = dt.datetime(2021, 1, 1)
        freqFilePath = getExcelFilePath(freqFileMapping, targetMonth)
        freqRecords = getFreqData(freqVoltConfigs, freqFilePath)
        print(freqRecords)
        self.assertTrue(freqRecords is not None)
        self.assertFalse(len(freqRecords) == 0)
