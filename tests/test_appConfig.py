import unittest
from src.config.appConfig import loadFileMappings


class TestAppConfig(unittest.TestCase):
    def test_fileMappings(self) -> None:
        """tests the function that tests file mappings config
        """
        fileMappings = loadFileMappings()
        self.assertTrue(fileMappings is not None)
        self.assertFalse(len(fileMappings) == 0)
