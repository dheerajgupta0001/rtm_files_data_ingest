CREATE TABLE MO_WAREHOUSE.PXI_RTM (
	ID NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY,
	TIME_STAMP DATE,
	col_attributes VARCHAR2(250),
	data_VALUE NUMBER(25,4),
    UNIQUE(time_stamp,col_attributes)
);