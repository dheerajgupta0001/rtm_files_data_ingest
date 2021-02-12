import pandas as pd
import json
from src.typeDefs.fileInfo import IFileInfo
from src.typeDefs.stateConfig import IStateConfig
from typing import List

fileMappings: List[IFileInfo] = []
stateConfigs: List[IStateConfig] = []

jsonConfig: dict = {}

def initConfigs():
    loadFileMappings()
    loadStatesConfig()
    loadJsonConfig()

def loadJsonConfig(fName="config.json") -> dict:
    global jsonConfig
    with open(fName) as f:
        data = json.load(f)
        jsonConfig = data
        return jsonConfig

def loadFileMappings(filePath='config.xlsx', sheetname='files_info') -> List[IFileInfo]:
    global fileMappings
    fileMappingsDf = pd.read_excel(filePath, sheet_name=sheetname)
    # Convert Nan to None
    # fileMappings = fileMappingsDf.where(pd.notnull(fileMappings),None)
    fileMappings = fileMappingsDf.to_dict('records')
    return fileMappings

def loadStatesConfig(filePath='config.xlsx', sheetname='states') -> List[IStateConfig]:
    global stateConfigs
    stateConfigsDf = pd.read_excel(filePath, sheet_name=sheetname)
    stateConfigs = stateConfigsDf.to_dict('records')
    return stateConfigs

def getFileMappings() -> List[IFileInfo]:
    global fileMappings
    return fileMappings


def getJsonConfig() -> dict:
    global jsonConfig
    return jsonConfig

def getStateConfigs() -> dict:
    global stateConfigs
    return stateConfigs