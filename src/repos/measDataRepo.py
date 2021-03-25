from typing import List
from src.typeDefs.iexGtamRecord import IIexGtamDataRecord
from src.repos.insertIexGtamMetricData import insertIexGtamData


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