import requests
import krakenex 
import praw 
import re 
from bs4 import BeautifulSoup
import json 
import pandas as pd
import s3fs
import boto3
import matplotlib.pyplot as plt


def get_data(event=None,context=None):
    ##################################################################################################################################
                #       Exchange orderbook Bias         #



    print('Starting scraping')
            ###########   CoinbasePro  ##################

    # Request order book data form API
    r = requests.get('https://api.pro.coinbase.com/products/BTC-USD/book?level=3' )
    r = r.content
    data = json.loads(r)

    # Define bids and asks form json data supplied via API
    bids = (data['bids'])
    asks = (data['asks'])

    ## Prase through the data to calculate total bid and ask volumes 
    coinbasepro_bid_vol = 0
    coinbasepro_ask_vol = 0
    for order in bids:
        coinbasepro_bid_vol += float(order[1])
    for order in asks:
        coinbasepro_ask_vol += float(order[1])


        ## Data to plot 
    #labels = 'Bids', 'Asks'
    sizes = [coinbasepro_bid_vol, coinbasepro_ask_vol]
    colors = ['green', 'red']

    ## Plot 
    plt.pie(sizes, colors = colors,
            autopct = '%1.1f%%', shadow = True, startangle = 90)
    plt.legend([f'{coinbasepro_bid_vol} BTC of Buying Volume' , f'{coinbasepro_ask_vol} BTC of Selling Volume'], bbox_to_anchor=(0,1), loc="center", 
                            bbox_transform=plt.gcf().transFigure)



  
    # Save graph to EC2 temp directory
    plt.savefig('/tmp/CoinbasePro_OrderBook1.png', bbox_inches = 'tight', transparent = True)

    s3_client = boto3.client('s3')
    # Upload graph to s3 bucket
    s3_client.upload_file('/tmp/CoinbasePro_OrderBook1.png', 'crypto-data-bucket' , 'static/CoinbasePro_OrderBook1.png')
    plt.clf()





            #################    Binance    ###############

    ## Request order book data form API    
    payload = {'symbol': 'BTCUSDT', 'limit': '100000000' }
    r = requests.get('https://api.binance.com/api/v3/depth', params = payload)
    r = r.content
    data = json.loads(r)


    bids = (data['bids'])
    asks = (data['asks'])



    ## Prase through the data to calculate total bid and ask volumes 
    binance_bid_vol = 0
    binance_ask_vol = 0
    for order in bids:
        binance_bid_vol += float(order[1])
    for order in asks:
        binance_ask_vol += float(order[1])

        ## Data to plot 
    #labels = 'Bids', 'Asks'
    sizes = [binance_bid_vol, binance_ask_vol]
    colors = ['green', 'red']

    ## Plot 
    plt.pie(sizes, colors = colors,
            autopct = '%1.1f%%', shadow = True, startangle = 90)
    plt.legend([f'{binance_bid_vol} BTC of Buying Volume' , f'{binance_ask_vol} BTC of Selling Volume'], bbox_to_anchor=(0,1), loc="center", 
                            bbox_transform=plt.gcf().transFigure)


  
    # Save graph to EC2 temp directory
    plt.savefig('/tmp/Binance_OrderBook1.png', bbox_inches = 'tight', trasnparent = True)

    s3_client = boto3.client('s3')
    # Upload graph to s3 bucket
    s3_client.upload_file('/tmp/Binance_OrderBook1.png', 'crypto-data-bucket' ,'static/Binance_OrderBook1.png')
    plt.clf()



        #####################    Kraken    #######################


    ## Request order book data form API    
    kraken = krakenex.API()
    response = kraken.query_public('Depth', {'pair': 'XXBTZUSD', 'count': '1000000000'})

    asks = response['result']['XXBTZUSD']['asks']
    bids = response['result']['XXBTZUSD']['bids']

    ## Prase through the data to calculate total bid and ask volumes 
    kraken_bid_vol = 0
    kraken_ask_vol = 0
    for order in bids:
        kraken_bid_vol += float(order[1])
    for order in asks:
        kraken_ask_vol += float(order[1])





            ## Data to plot 
    #labels = 'Bids', 'Asks'
    sizes = [kraken_bid_vol, kraken_ask_vol]
    colors = ['green', 'red']

    ## Plot 
    plt.pie(sizes, colors = colors,
            autopct = '%1.1f%%', shadow = True, startangle = 90)
    plt.legend([f'{kraken_bid_vol} BTC of Buying Volume' , f'{kraken_ask_vol} BTC of Selling Volume'], bbox_to_anchor=(0,1), loc="center", 
                            bbox_transform=plt.gcf().transFigure)


  
    # Save graph to EC2 temp directory
    plt.savefig('/tmp/Kraken_OrderBook1.png', bbox_inches = 'tight', trasnparent = True)

    s3_client = boto3.client('s3')
    # Upload graph to s3 bucket
    s3_client.upload_file('/tmp/Kraken_OrderBook1.png', 'crypto-data-bucket' ,'static/Kraken_OrderBook1.png')
    plt.clf()






                        ##########     Poloniex   ##########

    ## Request order book data form API    
    r = requests.get('https://poloniex.com/public?command=returnOrderBook&currencyPair=USDT_BTC&depth=100000000')
    r = r.content


    data = json.loads(r)


    bids = (data['bids'])
    asks = (data['asks'])


    ## Prase through the data to calculate total bid and ask volumes 
    poloniex_bid_vol = 0
    poloniex_ask_vol = 0
    for order in bids:
        poloniex_bid_vol += float(order[1])
    for order in asks:
        poloniex_ask_vol += float(order[1])






                ## Data to plot 
    #labels = 'Bids', 'Asks'
    sizes = [poloniex_bid_vol, poloniex_ask_vol]
    colors = ['green', 'red']

    ## Plot 
    plt.pie(sizes, colors = colors,
            autopct = '%1.1f%%', shadow = True, startangle = 90)
    plt.legend([f'{poloniex_bid_vol} BTC of Buying Volume' , f'{poloniex_ask_vol} BTC of Selling Volume'], bbox_to_anchor=(0,1), loc="center", 
                            bbox_transform=plt.gcf().transFigure)


  
    # Save graph to EC2 temp directory
    plt.savefig('/tmp/Poloniex_OrderBook1.png', bbox_inches = 'tight', trasnparent = True)

    s3_client = boto3.client('s3')
    # Upload graph to s3 bucket
    s3_client.upload_file('/tmp/Poloniex_OrderBook1.png', 'crypto-data-bucket' ,'static/Poloniex_OrderBook1.png')
    plt.clf()




            ####################      BITREX      #####################



    ## Request order book data form API
    r = requests.get('https://api.bittrex.com/api/v1.1/public/getorderbook?market=USD-BTC&type=both')
    r = r.content
    data = json.loads(r)


    bids = (data['result']['buy'])
    asks = (data['result']['sell'])


    ## Prase through the data to calculate total bid and ask volumes 
    bitrex_bid_vol = 0
    bitrex_ask_vol = 0
    for order in bids:
        bitrex_bid_vol += float(order['Quantity'])
    for order in asks:
        bitrex_ask_vol += float(order['Quantity'])


                  ## Data to plot 
    #labels = 'Bids', 'Asks'
    sizes = [bitrex_bid_vol, bitrex_ask_vol]
    colors = ['green', 'red']

    ## Plot 
    plt.pie(sizes, colors = colors,
            autopct = '%1.1f%%', shadow = True, startangle = 90)
    plt.legend([f'{bitrex_bid_vol} BTC of Buying Volume' , f'{bitrex_ask_vol} BTC of Selling Volume'], bbox_to_anchor=(0,1), loc="center", 
                            bbox_transform=plt.gcf().transFigure)


  
    # Save graph to EC2 temp directory
    plt.savefig('/tmp/Bitrexx_OrderBook1.png', bbox_inches = 'tight', trasnparent = True)

    s3_client = boto3.client('s3')
    # Upload graph to s3 bucket
    s3_client.upload_file('/tmp/Bitrexx_OrderBook1.png', 'crypto-data-bucket' ,'static/Bitrexx_OrderBook1.png')
    plt.clf()





    ################################################################################################################################
                #       Tradingview longs vs shorts         #




    page = 1
    longs = 0
    shorts = 0 

    for i in range(30):
        url = requests.get(str(f"https://www.tradingview.com/ideas/btc/page-{page}/")).text
        soup = BeautifulSoup(url, 'html.parser')
        
        # Find all trade ideas
        posts = soup.find_all('div', class_ = 'tv-widget-idea js-userlink-popup-anchor')
        
        # For each idea, check to see if it is a Long trade or Short trade
        for div in posts:
            long = soup.find_all('span', class_ = 'tv-idea-label tv-widget-idea__label tv-idea-label--long')
            short = soup.find_all('span', class_ = 'tv-idea-label tv-widget-idea__label tv-idea-label--short')
        
        # Append the amount of long or short trades to the long and short variables 
        longs += len(long)
        shorts += len(short)
        
        # Edit the url param to be the next page.
        page += 1



        ## Data to plot 
    sizes = [longs, shorts]
    colors = ['green', 'red']

    ## Plot 
    plt.pie(sizes, colors = colors,
            autopct = '%1.1f%%', shadow = True, startangle = 90)
    plt.legend([f'{longs} long trade ideas' , f'{shorts} short trade ideas'], bbox_to_anchor=(0,1), loc= 'best', 
                                bbox_transform=plt.gcf().transFigure)


    # Save graph to EC2 temp directory
    plt.savefig('/tmp/Long_vs_Short.png', bbox_inches = 'tight', trasnparent = True)

    s3_client = boto3.client('s3')
    # Upload graph to s3 bucket
    s3_client.upload_file('/tmp/Long_vs_Short.png', 'crypto-data-bucket' ,'static/Long_vs_Short.png')
    plt.clf()



    #######################################################################################################################
                #       reddit instances         ##



    # Variabls to append
    xmr = []
    eth = []
    btc = [] 
    xrp = []
    dash = []
    ltc = []

    # Instance of the Praw API wrapper
    reddit = praw.Reddit(client_id = 'AoHzLWcDDleGWw', client_secret = 'iI6QbcM2Z1CVod0j_gzBbumkHaU',
                        username ='germanp34e', password = 'red1234it', user_agent = 'agent')

    # Define the subredit and ammount of posts to scrape
    subreddit = reddit.subreddit('CryptoCurrency')
    recent_posts = subreddit.hot(limit = 300)

    # Loop through each post
    for post in recent_posts:
        # Try scraping for Btc
        try: 
            btc.append(re.search(r'btc|bitcoin', post.selftext, flags = re.IGNORECASE).group())
        except AttributeError: 
            pass
        
        # Try scraping for Xmr
        try:
            xmr.append(re.search(r'xmr|monero', post.selftext, flags = re.IGNORECASE).group())
            
        except AttributeError:
            pass
        
        # Try scraping for Xrp
        try:
            xrp.append(re.search(r'xrp|ripple', post.selftext, flags = re.IGNORECASE).group())
            
        except AttributeError:
            pass

        # Try scraping for Eth
        try:
            eth.append(re.search(r'eth|ethereum', post.selftext, flags = re.IGNORECASE).group())
            
        except AttributeError:
            pass
        
        # Try scraping for Dash
        try:
            dash.append(re.search(r'dash', post.selftext, flags = re.IGNORECASE).group())
        except AttributeError:
            pass
        
        # Try scraping for Ltc
        try:
            ltc.append(re.search(r'ltc|litecoin', post.selftext, flags = re.IGNORECASE).group())
        except AttributeError:
            pass

    xmr = len(xmr)
    eth = len(eth)
    btc = len(btc)
    xrp = len(xrp)
    dash = len(dash)
    ltc = len(ltc)

    # Create names and values to plot    
    names = ['Bitcoin','Monero','Ethereum','Ripple','Litecoin','Dash']
    values = [btc, xmr, eth, xrp, ltc, dash]

    # Create plot from names and values
    plt.clf()
    plt.style.use('classic')
    plt.bar(names,values)

        # Save graph to EC2 temp directory
    plt.savefig('/tmp/reddit_postss.png', bbox_inches = 'tight')

    s3_client = boto3.client('s3')
    # Upload graph to s3 bucket
    s3_client.upload_file('/tmp/reddit_postss.png', 'crypto-data-bucket' ,'static/reddit_postss.png')
    plt.clf()


    print('Data Scraped')
    
    df = pd.DataFrame({'tradingview_longs': [longs], 'tradingview_shorts': [shorts], 'coinbasepro_orderbook_bids': [coinbasepro_bid_vol], 'coinbasepro_orderbook_asks': [coinbasepro_ask_vol], 'binance_orderbook_bids': [binance_bid_vol], 'binance_orderbook_asks': [binance_ask_vol], 'kraken_orderbook_bids': [kraken_bid_vol], 'kraken_orderbook_asks': [kraken_ask_vol], 'bitrex_orderbook_bids': [bitrex_bid_vol], 'bitrex_orderbook_asks': [bitrex_ask_vol], 'poloniex_orderbook_bids': [poloniex_bid_vol], 'poloniex_orderbook_asks': [poloniex_ask_vol], 'reddit_inst_btc': [btc], 'reddit_inst_eth': [eth], 'reddit_inst_xmr': [xmr], 'reddit_inst_xrp': [xrp], 'reddit_inst_ltc': [ltc], 'reddit_inst_dash': [dash], 'id': [1]})
    

    df.to_csv('s3://crypto-data-bucket/crypto_db_data.csv', index=False)

    print('Tried to write to s3')
