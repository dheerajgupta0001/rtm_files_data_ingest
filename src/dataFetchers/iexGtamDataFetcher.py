import pandas as pd
import datetime as dt
from typing import Dict
from typing import List
from src.typeDefs.iexGtamRecord import IIexGtamDataRecord
from functools import reduce


def getIexGtamData(targetFilePath: str):

    derDf = pd.DataFrame()

    dataSheetDf = pd.read_excel(
        targetFilePath, sheet_name="DateWiseTrade", skiprows=3)
    dataSheetDf = dataSheetDf.dropna(axis=1, how='all')
    dataSheetDf['Trade Date'].fillna(
        value=dataSheetDf.loc[0, 'Trade Date'], inplace=True)
    dataSheetDf[['contract_type', 'A', 'B']
                ] = dataSheetDf['Instrument Name'].str.split('-', expand=True)

    derDfDate = dataSheetDf['Trade Date']

    dataSheetDf.drop(['Contract Type', 'A', 'B', 'Opening Price', 'Closing/Equilibrium Price (Rs/MWh) ', 'Next Best Buy Bid Available',
                      'Next Best Sell Bid Available', 'Duration', 'Region', 'Total Traded Volume MW'], axis=1, inplace=True)
    dataSheetDf = pd.melt(dataSheetDf, id_vars=[
                          'Trade Date', 'Instrument Name', 'contract_type'])
    dataSheetDf = dataSheetDf.rename(columns={
                                     'variable': 'metric_name', 'value': 'data_val', 'Trade Date': 'date_time', 'Instrument Name': 'instrument_name'})
    dataSheetDf['data_val'].fillna(0, inplace=True)
    for i in range(len(dataSheetDf['data_val'])):
        if dataSheetDf['data_val'][i] == '--':
            dataSheetDf['data_val'][i] = 0
        if (type(dataSheetDf['data_val'][i]) != float) and (type(dataSheetDf['data_val'][i]) != int):
            dataSheetDf['data_val'][i] = float(dataSheetDf['data_val'][i])
    dataSheetDf['data_val'] = dataSheetDf['data_val'].astype('float64')
    iexGtamRecords = dataSheetDf.to_dict('records')

    testDerDf = dataSheetDf.pivot(
        index=('date_time', 'instrument_name', 'contract_type'), columns='metric_name', values='data_val')
    testDerDf.reset_index(inplace=True)
    testDerDf[['A', 'B', 'ns_sl']] = testDerDf['instrument_name'].str.split(
        '-', expand=True)
    testDerDf.drop(['A', 'B', 'instrument_name', 'date_time'],
                   axis=1, inplace=True)

    highestPriceDf = testDerDf.groupby(['contract_type', 'ns_sl']).max()
    highestPriceDf.drop(['Lowest Price', 'Total Traded Volume (MWh)',
                         'Total Buy Bid Volume (MWh)', 'Total Sell Bid Volume (MWh)'], axis=1, inplace=True)
    lowestPriceDf = testDerDf.groupby(['contract_type', 'ns_sl']).min()
    lowestPriceDf.drop(['Highest Price', 'Total Traded Volume (MWh)', 'No of Trades',
                        'Total Buy Bid Volume (MWh)', 'Total Sell Bid Volume (MWh)'], axis=1, inplace=True)
    totalTradesPerDayDf = testDerDf.groupby(['contract_type', 'ns_sl']).sum()
    totalTradesPerDayDf.drop(['Highest Price', 'Lowest Price', 'Total Buy Bid Volume (MWh)',
                              'Total Sell Bid Volume (MWh)'], axis=1, inplace=True)
    highestPriceDf.reset_index(inplace=True)
    lowestPriceDf.reset_index(inplace=True)
    totalTradesPerDayDf.reset_index(inplace=True)

    data_frames = [highestPriceDf, lowestPriceDf, totalTradesPerDayDf]
    df_merged = reduce(lambda left, right: pd.merge(left, right, on=['contract_type', 'ns_sl'],
                                                    how='outer'), data_frames)

    overallHighestPriceDf = df_merged.groupby(['contract_type']).max()
    overallHighestPriceDf.drop(
        ['Lowest Price', 'Total Traded Volume (MWh)', 'No of Trades_y', 'ns_sl'], axis=1, inplace=True)
    overallHighestPriceDf.reset_index(inplace=True)
    overallLowestPriceDf = df_merged.groupby(['contract_type']).min()
    overallLowestPriceDf.drop(['Highest Price', 'Total Traded Volume (MWh)',
                               'No of Trades_y', 'No of Trades_x', 'ns_sl'], axis=1, inplace=True)
    overallLowestPriceDf.reset_index(inplace=True)
    overallTotalDf = df_merged.groupby(['contract_type']).sum()
    overallTotalDf.drop(['Highest Price', 'No of Trades_x',
                         'Lowest Price'], axis=1, inplace=True)
    overallTotalDf.reset_index(inplace=True)
    dac_int_df = [overallHighestPriceDf, overallLowestPriceDf, overallTotalDf]
    df_contract_merged = reduce(lambda left, right: pd.merge(left, right, on=['contract_type'],
                                                             how='outer'), dac_int_df)
    df_merged['contract_type'] = df_merged["contract_type"] + \
        "-" + df_merged["ns_sl"]
    df_merged.drop(['ns_sl'], axis=1, inplace=True)
    df_contract_merged = df_contract_merged.append(df_merged)
    df_contract_merged['time_stamp'] = derDfDate

    df_contract_merged = df_contract_merged.rename(columns={
        'Highest Price': 'highest_price', 'No of Trades_x': 'max_trades',
        'Lowest Price': 'lowest_price', 'No of Trades_y': 'total_trades',
        'Total Traded Volume (MWh)': 'total_traded_vol'})
    iexGtamTableRecords = df_contract_merged.to_dict('records')

    return iexGtamRecords, iexGtamTableRecords
