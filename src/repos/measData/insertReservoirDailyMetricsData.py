from typing_extensions import final
import cx_Oracle
from typing import List
from src.typeDefs.reservoirMeasRecord import IReservoirDataRecord


def insertReservoirDailyMetricsData(appDbConnStr: str, dataSamples: List[IReservoirDataRecord]) -> bool:
    """Inserts a entity metrics time series data into the app db

    Args:
    appDbConnStr (str): [description]
    dataSamples (List[IReservoirDataRecord]): [description]

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
        keyNames = ['data_time', 'entity_tag', 'metric_tag', 'data_val']
        colsNames = ["TIME_STAMP", "ENTITY_TAG", "METRIC_TAG", "DATA_VALUE"]
        sqlPlaceHldrsTxt = ','.join([':{0}'.format(x+1)
                                     for x in range(len(colsNames))])
        # delete the rows which are already present
        existingEntityRecords = [(x['data_time'], x['entity_tag'], x['metric_tag'])
                                 for x in dataSamples]
        dbCur.execute(
            "ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD HH24:MI:SS' ")
        dbCur.executemany(
            "delete from MIS_WAREHOUSE.RESERVOIR_DAILY_DATA \
                    where TIME_STAMP=:1 and ENTITY_TAG=:2 \
                    and METRIC_TAG= :3", existingEntityRecords)
        # insert the raw data
        sql_insert = "insert into MIS_WAREHOUSE.RESERVOIR_DAILY_DATA({0}) values ({1})".format(
            ','.join(colsNames), sqlPlaceHldrsTxt)

        dbCur.executemany(sql_insert, [tuple(
            [r[col] for col in keyNames]) for r in dataSamples])
        # commit the changes
        dbConn.commit()

    except Exception as err:
        isInsertSuccess = False
        print('Error while insertion of Reservoir Daily Metric Data')
        print(err)

    finally:
        if dbCur is not None:
            dbCur.close()
        if dbConn is not None:
            dbConn.close()

    return isInsertSuccess
