from typing import List
from src.typeDefs.iexGtamRecord import IIexGtamDataRecord
from src.typeDefs.iexGdamRecord import IIexGdamDataRecord
from src.repos.insertIexGtamMetricData import insertIexGtamData
from src.repos.insertIexGtamDeriveMetricData import insertIexGtamDeriveData

from src.repos.insertIexRtmMetricData import insertIexRtmData
from src.repos.insertIexDamMetricData import insertIexDamData
from src.repos.insertIexGdamMetricData import insertIexGdamData
from src.repos.insertPxiDamMetricData import insertPxiDamData
from src.repos.insertPxiRtmMetricData import insertPxiRtmData
from src.repos.insertWbesRtmIexMetricData import insertWbesRtmIexData
from src.repos.insertWbesRtmPxiMetricData import insertWbesRtmPxiData
from src.repos.insertWbesPxPxiMetricData import insertWbesPxPxiData
from src.repos.insertWbesPxIexMetricData import insertWbesPxIexData



class MeasDataRepo():
    """Repository class for entity metrics data
    """
    appDbConnStr: str = ""

    def __init__(self, dbConStr: str) -> None:
        """constructor method
        Args:
            dbConStr (str): database connection string
        """
        self.appDbConnStr = dbConStr

    def insertIexGtamData(self, dataSamples: List[IIexGtamDataRecord]) -> bool:
        """inserts a entity metrics time series data into the app db
        Returns:
            bool: returns true if process is ok
        """
        return insertIexGtamData(self.appDbConnStr, dataSamples)
    def insertIexGtamDeriveData(self, dataSamples: List[IIexGtamDataRecord]) -> bool:
        """inserts a entity metrics time series data into the app db
        Returns:
            bool: returns true if process is ok
        """
        return insertIexGtamDeriveData(self.appDbConnStr, dataSamples)

    def insertIexRtmData(self, dataSamples: List[IIexGtamDataRecord]) -> bool:
        """inserts a entity metrics time series data into the app db
        Returns:
            bool: returns true if process is ok
        """
        return insertIexRtmData(self.appDbConnStr, dataSamples)

    def insertIexDamData(self, dataSamples: List[IIexGtamDataRecord]) -> bool:
        """inserts a entity metrics time series data into the app db
        Returns:
            bool: returns true if process is ok
        """
        return insertIexDamData(self.appDbConnStr, dataSamples)

    def insertIexGdamData(self, dataSamples: List[IIexGdamDataRecord]) -> bool:
        """inserts a entity metrics time series data into the app db
        Returns:
            bool: returns true if process is ok
        """
        return insertIexGdamData(self.appDbConnStr, dataSamples)

    def insertPxiDamData(self, dataSamples: List[IIexGtamDataRecord]) -> bool:
        """inserts a entity metrics time series data into the app db
        Returns:
            bool: returns true if process is ok
        """
        return insertPxiDamData(self.appDbConnStr, dataSamples)

    def insertPxiRtmData(self, dataSamples: List[IIexGtamDataRecord]) -> bool:
        """inserts a entity metrics time series data into the app db
        Returns:
            bool: returns true if process is ok
        """
        return insertPxiRtmData(self.appDbConnStr, dataSamples)

    def insertWbesRtmIexData(self, dataSamples: List[IIexGtamDataRecord]) -> bool:
        """inserts a entity metrics time series data into the app db
        Returns:
            bool: returns true if process is ok
        """
        return insertWbesRtmIexData(self.appDbConnStr, dataSamples)

    def insertWbesRtmPxiData(self, dataSamples: List[IIexGtamDataRecord]) -> bool:
        """inserts a entity metrics time series data into the app db
        Returns:
            bool: returns true if process is ok
        """
        return insertWbesRtmPxiData(self.appDbConnStr, dataSamples)
    def insertWbesPxPxiData(self, dataSamples: List[IIexGtamDataRecord]) -> bool:
        """inserts a entity metrics time series data into the app db
        Returns:
            bool: returns true if process is ok
        """
        return insertWbesPxPxiData(self.appDbConnStr, dataSamples)
    def insertWbesPxIexData(self, dataSamples: List[IIexGtamDataRecord]) -> bool:
        """inserts a entity metrics time series data into the app db
        Returns:
            bool: returns true if process is ok
        """
        return insertWbesPxIexData(self.appDbConnStr, dataSamples)