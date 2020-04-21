# fill_db.py

import pandas as pd 
import s3fs 
import psycopg2



def fill_data(context=None, event=None):
    data = pd.read_csv('s3://crypto-data-bucket/crypto_db_data.csv')



    con = psycopg2.connect( host = 'db location on aws',
                            database = 'db instance name',
                            user = 'username for db access',
                            password = 'db password',
                            port = 'db port') 


    cur = con.cursor()

    print('connected')

    cur.execute('INSERT INTO crypto_data (tradingview_longs, tradingview_shorts, coinbasepro_orderbook_bids, coinbasepro_orderbook_asks, binance_orderbook_bids, binance_orderbook_asks, kraken_orderbook_bids, kraken_orderbook_asks, bitrex_orderbook_bids, bitrex_orderbook_asks, poloniex_orderbook_bids, poloniex_orderbook_asks, reddit_inst_btc, reddit_inst_eth, reddit_inst_xmr, reddit_inst_xrp, reddit_inst_ltc, reddit_inst_dash) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (int(data.iloc[0]['tradingview_longs']), int(data.iloc[0]['tradingview_shorts']), int(data.iloc[0]['coinbasepro_orderbook_bids']), int(data.iloc[0]['coinbasepro_orderbook_asks']), int(data.iloc[0]['binance_orderbook_bids']), int(data.iloc[0]['binance_orderbook_asks']), int(data.iloc[0]['kraken_orderbook_bids']), int(data.iloc[0]['kraken_orderbook_asks']), int(data.iloc[0]['bitrex_orderbook_bids']), int(data.iloc[0]['bitrex_orderbook_asks']), int(data.iloc[0]['poloniex_orderbook_bids']), int(data.iloc[0]['poloniex_orderbook_asks']), int(data.iloc[0]['reddit_inst_btc']), int(data.iloc[0]['reddit_inst_eth']), int(data.iloc[0]['reddit_inst_xmr']), int(data.iloc[0]['reddit_inst_xrp']), int(data.iloc[0]['reddit_inst_ltc']), int(data.iloc[0]['reddit_inst_dash'])))

    con.commit()

    con.close()