# make_corr_plots.py

'''
This script is to be run as a lambda function on AWS. 
It acceses a AWS RDS instance, reads info and creates plots with matplotlib. 
These plost are then saved to an AWS s3 bucket. 
'''


import psycopg2
import yfinance as yf
from matplotlib import pyplot as plt
import s3fs
import boto3
import datetime

class Data_fetcher:
    def __init__(self):
        pass
         
    # Connect to aws db instance and querry the crypto-data table for column name passed into the function.    
    def get_data(self,column):  
        con = psycopg2.connect( host = 'cryptodb.cujx43zpek8h.us-east-1.rds.amazonaws.com',
                                database = 'postgres',
                                user = 'postgres',
                                password = 'pg1234321.',
                                port = '5432') 

        cur = con.cursor()

        cur.execute(f'SELECT {column} FROM crypto_data')

        values = cur.fetchall()
        values_list = []
        # Values are returned from DB as tuples. Use a quick loop to make a list 'values_list' of integer values
        for i in range(len(values)):
            values_list.append(values[i][0])
        return values_list
    
        con.commit()

        con.close()





def corr_plot(ticker, db_col):
    # Make a list 'price_data' of daily closing prices of the ticker passed as the first argument
    today = datetime.date.today()
    tic = yf.Ticker(ticker)
    price_data = []
    prices = tic.history(start = '2020-03-12', end = today)
    for i in range(len(prices)):
        price_data.append(prices.Close[i])

    days = len(price_data)

    # Create an instance of the Data_fetcher() class
    data_fetch = Data_fetcher()

    # Save the values_list returned by the data_fetch.getdata() function as a variable called values
    values = data_fetch.get_data(db_col)


    # setup, create and save plot to AWS S3 bucket
    fig, ax1 = plt.subplots()

    # First x and y axis
    color = 'tab:red'
    ax1.set_xlabel('Time (Days)')
    ax1.set_title(f'{ticker}', fontsize = 'x-large')
    ax1.set_ylabel(ticker, color = color)
    ax1.plot(price_data, color = color)
    ax1.tick_params(axis='y', labelcolor = color)

    # instantiate a secon axes that shares the same x-axis
    ax2 = ax1.twinx()

    # second x axis info, no y aixis needed bucasue it is defined above and is shared
    color = 'tab:blue'
    ax2.set_ylabel( db_col.title(), color = color)
    ax2.plot(values, color = 'tab:blue')
    ax2.tick_params(axis='y', labelcolor = color)
    
    # save graph to s3 locaiton
    fig.tight_layout()

    plt.savefig(f'/tmp/{db_col}_corr.png', bbox_inches = 'tight', transparent = True)

    s3_client = boto3.client('s3')

    s3_client.upload_file(f'/tmp/{db_col}_corr.png', 'crypto-data-bucket' ,f'static/{db_col}_corr.png')

# Call the corr_plot for all the rows in the DB
def make_plots(event=None, context=None):
    corr_plot('BTC-USD', 'tradingview_longs')
    corr_plot('BTC-USD', 'tradingview_shorts')
    corr_plot('BTC-USD', 'coinbasepro_orderbook_bids')
    corr_plot('BTC-USD', 'coinbasepro_orderbook_asks')
    corr_plot('BTC-USD', 'binance_orderbook_bids')
    corr_plot('BTC-USD', 'binance_orderbook_asks')
    corr_plot('BTC-USD', 'kraken_orderbook_bids')
    corr_plot('BTC-USD', 'kraken_orderbook_asks')
    corr_plot('BTC-USD', 'bitrex_orderbook_bids')
    corr_plot('BTC-USD', 'bitrex_orderbook_asks')
    corr_plot('BTC-USD', 'poloniex_orderbook_bids')
    corr_plot('BTC-USD', 'poloniex_orderbook_asks')
    corr_plot('BTC-USD', 'reddit_inst_btc')
    corr_plot('ETH-USD', 'reddit_inst_eth')
    corr_plot('XMR-USD', 'reddit_inst_xmr')
    corr_plot('LTC-USD', 'reddit_inst_ltc')
    corr_plot('XRP-USD', 'reddit_inst_xrp')
    corr_plot('DASH-USD', 'reddit_inst_dash')

   
