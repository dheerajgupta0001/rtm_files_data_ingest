from typing_extensions import final
import cx_Oracle
from typing import List
from src.typeDefs.iexDamRecord import IIexDamDataRecord


def insertIexDamData(appDbConnStr: str, dataSamples: List[IIexDamDataRecord]) -> bool:
    """Inserts a entity metrics time series data into the app db

    Args:
    appDbConnStr (str): [description]
    dataSamples (List[IMetricsDataRecord]): [description]

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
        keyNames = ['date_time', 'metric_name', 'data_val']
        colsNames = ["TIME_STAMP", "col_attributes", "DATA_VALUE"]
        sqlPlaceHldrsTxt = ','.join([':{0}'.format(x+1)
                                     for x in range(len(colsNames))])
        # delete the rows which are already present
        existingEntityRecords = [(x['date_time'], x['metric_name'])
                                 for x in dataSamples]
        dbCur.execute(
            "ALTER SESSION SET NLS_DATE_FORMAT = 'DD-MM-YYYY HH24:MI:SS' ")
        dbCur.executemany(
            "delete from MO_WAREHOUSE.IEX_DAM where TIME_STAMP=:1 and col_attributes=:2", existingEntityRecords)
        # insert the raw data
        sql_insert = "insert into MO_WAREHOUSE.IEX_DAM({0}) values ({1})".format(
            ','.join(colsNames), sqlPlaceHldrsTxt)

        dbCur.executemany(sql_insert, [tuple(
            [r[col] for col in keyNames]) for r in dataSamples])
        # commit the changes
        dbConn.commit()

    except Exception as err:
        isInsertSuccess = False
        print('Error while insertion of Iex Dam Data')
        print(err)

    finally:
        if dbCur is not None:
            dbCur.close()
        if dbConn is not None:
            dbConn.close()

    return isInsertSuccess
