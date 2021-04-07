from typing_extensions import final
import cx_Oracle
from typing import List
from src.typeDefs.wbesRtmPxiRecord import IWbesRtmPxiDataRecord


def insertWbesPxPxiData(appDbConnStr: str, dataSamples: List[IWbesRtmPxiDataRecord]) -> bool:
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
        keyNames = ['date_time', 'beneficiary', 'data_val', 'beneficiary_type']
        colsNames = ["TIME_STAMP", "beneficiary", "DATA_VALUE", "beneficiary_type"]
        sqlPlaceHldrsTxt = ','.join([':{0}'.format(x+1)
                                     for x in range(len(colsNames))])
        # delete the rows which are already present
        existingEntityRecords = [(x['date_time'], x['beneficiary'], x['beneficiary_type'])
                                 for x in dataSamples]
        dbCur.execute(
            "ALTER SESSION SET NLS_DATE_FORMAT = 'DD-MM-YYYY HH24:MI:SS' ")
        dbCur.executemany(
                    "delete from MO_WAREHOUSE.WBES_PX_PXI where TIME_STAMP=:1\
                        and beneficiary=:2 and beneficiary_type=:3", existingEntityRecords)
        # insert the raw data
        sql_insert = "insert into MO_WAREHOUSE.WBES_PX_PXI({0}) values ({1})".format(
            ','.join(colsNames), sqlPlaceHldrsTxt)

        dbCur.executemany(sql_insert, [tuple(
            [r[col] for col in keyNames]) for r in dataSamples])
        # commit the changes
        dbConn.commit()

    except Exception as err:
        isInsertSuccess = False
        print('Error while insertion of WBES PX PXI Data')
        print(err)

    finally:
        if dbCur is not None:
            dbCur.close()
        if dbConn is not None:
            dbConn.close()

    return isInsertSuccess
