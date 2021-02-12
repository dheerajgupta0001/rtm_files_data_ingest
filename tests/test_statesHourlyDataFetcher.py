import unittest
from src.dataFetchers.statesHourlyDataFetcher import getStatesHourlyData


class TestGetStateHourlyData(unittest.TestCase):
    def test_stateHourlyData(self) -> None:
        """tests the function that tests file mappings config
        """
        statesData = getStatesHourlyData()
        self.assertTrue(statesData is not None)
        self.assertFalse(len(statesData) == 0)

