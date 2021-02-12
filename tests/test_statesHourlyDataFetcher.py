import unittest
from src.dataFetchers.statesHourlyDataFetcher import getStatesHourlyData


class TestGetStateHourlyData(unittest.TestCase):
    def test_stateHourlyData(self) -> None:
        """tests the function that tests file mappings config
        """
        statesData = getStatesHourlyData()
        self.assertTrue(statesData is not None)
        self.assertFalse(len(statesData) == 0)
<<<<<<< HEAD

=======
        
>>>>>>> d8ff720006d1aef0e742837879c1577d1f81c049
