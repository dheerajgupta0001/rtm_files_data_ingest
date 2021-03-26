from typing import List
from src.typeDefs.iexGtamRecord import IIexGtamDataRecord
from src.repos.insertIexGtamMetricData import insertIexGtamData
from src.repos.insertIexRtmMetricData import insertIexRtmData
from src.repos.insertIexDamMetricData import insertIexDamData


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