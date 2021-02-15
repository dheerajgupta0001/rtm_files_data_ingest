from typing_extensions import final
import cx_Oracle
from typing import List
from src.typeDefs.freqRecord import IFreqDataRecord


def insertDaywiseFreqMetrics(appDbConnStr: str, dataSamples: List[IFreqDataRecord]) -> bool:
    """Inserts a entity metrics time series data into the app db

    Args:
    appDbConnStr (str): [description]
    dataSamples (List[IFreqDataRecord]): [description]

    Returns:
        bool: returns true if process is ok
    """
    dbConn = None
    dbCur = None
    isInsertSuccess = True
    if len(dataSamples) == 0:
        return isInsertSuccess
    try:
        dbConn = cx_Oracle.connect(appDbConnStr)
        dbCur = dbConn.cursor()
        # keyNames names of the raw data
        keyNames = ['data_time', 'metric_name', 'data_val']
        colsNames = ["data_time","metric_name","data_val"]
        sqlPlaceHldrsTxt = ','.join([':{0}'.format(x+1)
                                     for x in range(len(colsNames))])
        # delete the rows which are already present
        existingFreqRecords = [(x['data_time'], x['metric_name'])
                                for x in dataSamples]
        dbCur.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD HH24:MI:SS' ")
        dbCur.executemany(
                "delete from MIS_WAREHOUSE.DAILY_FREQ_METRICS where data_time=:0 and metric_name=:1", existingFreqRecords)
        # insert the raw data
        sql_insert = "insert into MIS_WAREHOUSE.DAILY_FREQ_METRICS({0}) values ({1})".format(
            ','.join(colsNames), sqlPlaceHldrsTxt)

        dbCur.executemany(sql_insert, [tuple(
            [r[col] for col in keyNames]) for r in dataSamples])
        # commit the changes
        dbConn.commit()
    except Exception as err:
        isInsertSuccess = False
        print('Error while insertion of daily freq metrics')
        print(err)
    finally:
        if dbCur is not None:
            dbCur.close()
        if dbConn is not None:
            dbConn.close()
        
    return isInsertSuccess
