import pandas as pd
import json
from src.typeDefs.fileInfo import IFileInfo
from src.typeDefs.stateConfig import IStateConfig
from src.typeDefs.freqVoltConfig import IFreqVoltConfig
from typing import List

fileMappings: List[IFileInfo] = []
stateConfigs: List[IStateConfig] = []
freqVolConfigs: List[IFreqVoltConfig] = []

jsonConfig: dict = {}

def initConfigs():
    loadFileMappings()
    loadStatesConfig()
    loadFreqVoltConfigs()
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

def loadFreqVoltConfigs(filePath='config.xlsx', sheetname='freq_volt') -> List[IFreqVoltConfig]:
    global freqVolConfigs
    freqVolConfigDf = pd.read_excel(filePath, sheet_name=sheetname)
    freqVolConfigs = freqVolConfigDf.to_dict('records')
    return freqVolConfigs

def getFileMappings() -> List[IFileInfo]:
    global fileMappings
    return fileMappings


def getJsonConfig() -> dict:
    global jsonConfig
    return jsonConfig

def getStateConfigs() -> List[IStateConfig]:
    global stateConfigs
    return stateConfigs

def getFreqVoltConfigs() -> List[IFreqVoltConfig]:
    global freqVolConfigs
    return freqVolConfigs