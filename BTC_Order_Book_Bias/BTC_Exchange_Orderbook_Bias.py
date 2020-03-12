





#########        CoinbasePro       ########


import requests
import pandas as pd
import json
import matplotlib.pyplot as plt
import krakenex


## Request order book data form API    
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


## Save plot to staic/images directory
#plt.axis('equal')
plt.savefig('/Users/julianbaumgartner/Desktop/Python/BTC_Data/static/images/CoinbasePro_OrderBook1.png', bbox_inches = 'tight', trasnparent = True)
plt.clf()
#plt.show()







            #############           Binance        ###########



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


## Save plot to staic/images directory
#plt.axis('equal')
plt.savefig('/Users/julianbaumgartner/Desktop/Python/BTC_Data/static/images/Binance_OrderBook1.png', bbox_inches = 'tight', trasnparent = True)
plt.clf()
#plt.show()






                ############         Kraken      ########## 





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

## Save plot to staic/images directory
#plt.axis('equal')
plt.savefig('/Users/julianbaumgartner/Desktop/Python/BTC_Data/static/images/Kraken_OrderBook1.png', bbox_inches = 'tight', trasnparent = True)
plt.clf()
#plt.show()




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

## Save plot to staic/images directory
#plt.axis('equal')
plt.savefig('/Users/julianbaumgartner/Desktop/Python/BTC_Data/static/images/Poloniex_OrderBook1.png', bbox_inches = 'tight', trasnparent = True)
plt.clf()
#plt.show()



                        ############      BITREX      ###########



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

## Pie Chart Plot 
plt.pie(sizes, colors = colors,
        autopct = '%1.1f%%', shadow = True, startangle = 90)
plt.legend([f'{bitrex_bid_vol} BTC of Buying Volume' , f'{bitrex_ask_vol} BTC of Selling Volume'], bbox_to_anchor=(0,1), loc="center", 
                        bbox_transform=plt.gcf().transFigure)
## Save plot to staic/images directory
#plt.axis('equal')
plt.savefig('/Users/julianbaumgartner/Desktop/Python/BTC_Data/static/images/Bittrex_OrderBook1.png', bbox_inches = 'tight', trasnparent = True)
plt.clf()
#plt.show()




