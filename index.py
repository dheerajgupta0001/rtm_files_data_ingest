from src.config.appConfig import initConfigs
from src.config.appConfig import getFileMappings
from src.dataFetchers.dataFetcherHandler import getExcelFilePath
from src.utils.addMonths import addMonths
import datetime as dt
from src.app.iexDamService import iexDamService
from src.app.iexGdamService import iexGdamService
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

endDt = dt.datetime.now()
endDt = dt.datetime(endDt.year,endDt.month,endDt.day)
startDt = endDt - dt.timedelta(days=1)
endDt =  startDt
print(startDt)
startDt = dt.datetime(2022, 2, 17)
endDt = dt.datetime(2022, 2, 17)

targetDt = startDt
while targetDt <= endDt:
    print('processing for {0}'.format(targetDt))
    for eachrow in filesSheet:
        print(eachrow['file_type'])
        excelFilePath = getExcelFilePath(eachrow, targetDt)
        if eachrow['file_type'] == 'iex_gdam_data':
            try:
                iexGdamService(excelFilePath)
            except Exception as ex:
                print(ex)
        if eachrow['file_type'] == 'iex_dam_data':
            try:
                iexDamService(excelFilePath)
            except Exception as ex:
                print(ex)
        if eachrow['file_type'] == 'iex_gtam_data':
            try:
                iexGtamService(excelFilePath)
            except Exception as ex:
                print(ex)
        if eachrow['file_type'] == 'iex_rtm_data':
            try:
                iexRtmService(excelFilePath)
            except Exception as ex:
                print(ex)
        # if eachrow['file_type'] == 'pxi_dam_data':
        #     try:
        #         pxiDamService(excelFilePath)
        #     except Exception as ex:
        #         print(ex)
        # if eachrow['file_type'] == 'pxi_rtm_data':
        #     try:
        #         pxiRtmService(excelFilePath)
        #     except Exception as ex:
        #         print(ex)
        if eachrow['file_type'] == 'wbes_rtm_iex_data':
            try:
                wbesRtmIexService(excelFilePath, targetDt)
            except Exception as ex:
                print(ex)
        if eachrow['file_type'] == 'wbes_rtm_pxi_data':
            try:
                wbesRtmPxiService(excelFilePath, targetDt)
            except Exception as ex:
                print(ex)
        if eachrow['file_type'] == 'wbes_px_iex_data':
            try:
                wbesPxIexService(excelFilePath, targetDt)
            except Exception as ex:
                print(ex)
        if eachrow['file_type'] == 'wbes_px_pxi_data':
            try:
                wbesPxPxiService(excelFilePath, targetDt)
            except Exception as ex:
                print(ex)
       
    targetDt=targetDt+dt.timedelta(days=1)        
    
