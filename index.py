from src.config.appConfig import initConfigs
from src.config.appConfig import getFileMappings
from src.dataFetchers.dataFetcherHandler import getExcelFilePath
from src.utils.addMonths import addMonths
import datetime as dt
from src.app.iexDamService import iexDamService
from src.app.wbesRtmIexService import wbesRtmIexService

initConfigs()
filesSheet = getFileMappings()

startDt = dt.datetime(2021, 3, 1)
endDt = dt.datetime(2021, 3, 1)

targetDt = startDt
while targetDt <= endDt:
    print('processing for {0}'.format(targetDt))
    for eachrow in filesSheet:
        print(eachrow['file_type'])
        excelFilePath = getExcelFilePath(eachrow, targetDt)
        # if eachrow['file_type'] == 'iex_dam_data':
        #     iexDamService(excelFilePath)
        # if eachrow['file_type'] == 'iex_rtm_data':
        #     statesDailyService(statesConfigSheet, excelFilePath)
        # if eachrow['file_type'] == 'iex_gtam_data':
        #     linesGenService(statesConfigSheet, excelFilePath)
        # if eachrow['file_type'] == 'pxi_dam_data':
        #     statesHourlyService(statesConfigSheet, excelFilePath)
        # if eachrow['file_type'] == 'pxi_rtm_data':
        #     reservoirService(excelFilePath)
        if eachrow['file_type'] == 'wbes_rtm_iex_data':
            wbesRtmIexService(excelFilePath, targetDt)
        # if eachrow['file_type'] == 'wbes_rtm_pxi_data':
        #     gujREGenerationService(excelFilePath)
    targetDt = addMonths(targetDt, 1)
