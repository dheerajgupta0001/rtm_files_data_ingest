from src.DataFetcher.statesHourlyDataFetcher import getStatesHourlyData
from src.typeDefs.fileInfo import IFileInfo
import datetime as dt
from src.config.appConfig import getFileMappings

# TODO delete this
def getStatesHourlyData(fileInfo:IFileInfo, targetMonth:dt.datetime):
    
    return getStatesHourlyData(fileInfo , targetMonth)
