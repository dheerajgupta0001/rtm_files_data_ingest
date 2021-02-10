import pandas as pd
import json


fileMappings: List[IFileInfo] = []

jsonConfig: dict = {}

def initConfig():
    loadFileMappings()
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


def getFileMappings() -> List[IFileInfo]:
    global fileMappings
    return fileMappings



def getJsonConfig() -> dict:
    global jsonConfig
    return jsonConfig