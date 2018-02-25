from __future__ import division

import pandas as pd


def get_data(date):
    df1 = pd.read_csv('NVDA_trade.csv', sep=',')
    print(df1.head())
    df1['pre_price'] = df1['PRICE'].shift(1)
    df1['diff'] = df1['PRICE'] - df1['pre_price']
    diff = df1.loc[df1.DATE == date, ['diff']].dropna()
    diff.to_csv('%s_price_diff' % str(date), sep='\t', index=False)

    df2 = pd.read_csv('NVDA_quote.csv', sep=',')
    print(df2.head())
    df2 = df2.loc[(df2.DATE == date) & (df2['ASK'] > 0) & (df2['BID'] > 0), ['ASK', 'BID']]
    df2['spread'] = df2['ASK'] - df2['BID']
    spread = df2['spread'].dropna()
    spread.to_csv('%s_spread' % str(date), sep='\t', index=False)


get_data(20180103)
