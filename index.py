from src.config.appConfig import initConfigs
from src.config.appConfig import getFileMappings
from src.dataFetchers.dataFetcherHandler import getExcelFilePath
from src.utils.addMonths import addMonths
import datetime as dt
from src.app.iexDamService import iexDamService
from src.app.iexGtamService import iexGtamService
from src.app.iexRtmService import iexRtmService
from src.app.pxiDamService import pxiDamService
from src.app.pxiRtmService import pxiRtmService

from src.app.wbesRtmPxiService import wbesRtmPxiService

from src.app.wbesRtmIexService import wbesRtmIexService
from src.app.wbesPxIexService import wbesPxIexService
from src.app.wbesPxPxiService import wbesPxPxiService


initConfigs()
filesSheet = getFileMappings()

startDt = dt.datetime(2021, 4, 25)
endDt = dt.datetime(2021, 4, 25)

targetDt = startDt
while targetDt <= endDt:
    print('processing for {0}'.format(targetDt))
    for eachrow in filesSheet:
        print(eachrow['file_type'])
        excelFilePath = getExcelFilePath(eachrow, targetDt)
        if eachrow['file_type'] == 'iex_dam_data':
            iexDamService(excelFilePath)
        if eachrow['file_type'] == 'iex_gtam_data':
            iexGtamService(excelFilePath)
        if eachrow['file_type'] == 'iex_rtm_data':
            iexRtmService(excelFilePath)
        if eachrow['file_type'] == 'pxi_dam_data':
            pxiDamService(excelFilePath)
        if eachrow['file_type'] == 'pxi_rtm_data':
            pxiRtmService(excelFilePath)
        if eachrow['file_type'] == 'wbes_rtm_iex_data':
            wbesRtmIexService(excelFilePath, targetDt)
        if eachrow['file_type'] == 'wbes_rtm_pxi_data':
            wbesRtmPxiService(excelFilePath, targetDt)
        if eachrow['file_type'] == 'wbes_px_iex_data':
            wbesPxIexService(excelFilePath, targetDt)
        if eachrow['file_type'] == 'wbes_px_pxi_data':
            wbesPxPxiService(excelFilePath, targetDt)
       
    targetDt=targetDt+dt.timedelta(days=1)        
    
