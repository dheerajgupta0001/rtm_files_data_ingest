import datetime
from typing import List, Any
from src.typeDefs.measRecord import IMetricsDataRecord
from src.typeDefs.freqRecord import IFreqDataRecord
from src.typeDefs.voltRecord import IVoltDataRecord
from src.repos.measData.insertStatesHourlyMetricsData import insertMetricsData
from src.repos.measData.insertStatesDailyMetricsData import insertDailyMetricsData
from src.repos.measData.insertGenLinesDailyMetricsData import insertGenLinesDailyMetricsData
from src.repos.measData.insertDaywiseFreqMetrics import insertDaywiseFreqMetrics
from src.repos.measData.insertDaywiseVoltMetrics import insertDaywiseVoltMetrics


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

    def insertStatesHorlyData(self, dataSamples: List[IMetricsDataRecord]) -> bool:
        """inserts a entity metrics time series data into the app db
        Returns:
            bool: returns true if process is ok
        """
        return insertMetricsData(self.appDbConnStr, dataSamples)

    def insertStatesDailyData(self, dataSamples: List[IMetricsDataRecord]) -> bool:
        """inserts a entity metrics time series data into the app db
        Returns:
            bool: returns true if process is ok
        """
        return insertDailyMetricsData(self.appDbConnStr, dataSamples)

    def insertGenLinesDailyData(self, dataSamples: List[IMetricsDataRecord]) -> bool:
        """inserts a entity metrics time series data into the app db
        Returns:
            bool: returns true if process is ok
        """
        return insertGenLinesDailyMetricsData(self.appDbConnStr, dataSamples)

    def insertDaywiseFreqMetrics(self, dataSamples: List[IFreqDataRecord]) -> bool:
        """inserts a entity metrics time series data into the app db
        Returns:
            bool: returns true if process is ok
        """
        return insertDaywiseFreqMetrics(self.appDbConnStr, dataSamples)

    def insertDaywiseVoltMetrics(self, dataSamples: List[IVoltDataRecord]) -> bool:
        """inserts a entity metrics time series data into the app db
        Returns:
            bool: returns true if process is ok
        """
        return insertDaywiseVoltMetrics(self.appDbConnStr, dataSamples)
