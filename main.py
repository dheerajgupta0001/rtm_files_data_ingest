from src.config.appConfig import initConfigs
from src.config.appConfig import getStateConfigs,getFileMappings
from src.app.statesHourlyService import statesHourlyService
from src.app.statesDailyService import statesDailyService
from src.dataFetchers.dataFetcherHandler import getExcelFilePath
from src.app.linesGenService import linesGenService
from src.app.reservoirService import reservoirService
from src.app.gujREGenerationService import gujREGenerationService
import datetime as dt

initConfigs()
filesSheet = getFileMappings()
statesConfigSheet = getStateConfigs()

targetMonth = dt.datetime(2021,1,1) 


for eachrow in filesSheet:
    print(eachrow['file_type'])
    excelFilePath = getExcelFilePath(eachrow , targetMonth )
    if eachrow['file_type'] == 'state_hourly_data':
        pass
        # statesHourlyService(statesConfigSheet , excelFilePath)

    elif eachrow['file_type'] == 'state_daily_data':
        pass
        # statesDailyService(statesConfigSheet , excelFilePath)
    
    elif eachrow['file_type'] == 'gen_lines_daily_data':
        # linesGenService(statesConfigSheet , excelFilePath)
        pass

    elif eachrow['file_type'] == 'reservoir_data':
        # reservoirService(excelFilePath)
        pass

    elif eachrow['file_type'] == 'guj_RE_gen_daily_data':
        targetMonth = dt.datetime(2021,2,1) 
        excelFilePath = getExcelFilePath(eachrow , targetMonth)

        gujREGenerationService(excelFilePath)
        pass