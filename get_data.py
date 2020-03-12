import sys
sys.path.append('/Users/julianbaumgartner/Desktop/Python/BTC_Data/BTC_Order_Book_Bias')
sys.path.append('/Users/julianbaumgartner/Desktop/Python/BTC_Data/Long_vs_Short')
sys.path.append('/Users/julianbaumgartner/Desktop/Python/BTC_Data/Reddit_Crypto')
import BTC_Exchange_Orderbook_Bias
import TradingView_Long_vs_Short_Bias
import reddit_crypto
import psycopg2



BTC_Exchange_Orderbook_Bias
TradingView_Long_vs_Short_Bias
reddit_crypto


coinbasepro_bid_vol = BTC_Exchange_Orderbook_Bias.coinbasepro_bid_vol
coinbasepro_ask_vol = BTC_Exchange_Orderbook_Bias.coinbasepro_ask_vol

binance_bid_vol = BTC_Exchange_Orderbook_Bias.binance_bid_vol
binance_ask_vol = BTC_Exchange_Orderbook_Bias.binance_ask_vol

kraken_bid_vol = BTC_Exchange_Orderbook_Bias.kraken_bid_vol
kraken_ask_vol = BTC_Exchange_Orderbook_Bias.kraken_ask_vol

bitrex_bid_vol = BTC_Exchange_Orderbook_Bias.bitrex_bid_vol
bitrex_ask_vol = BTC_Exchange_Orderbook_Bias.bitrex_ask_vol

poloniex_bid_vol = BTC_Exchange_Orderbook_Bias.poloniex_bid_vol
poloniex_ask_vol = BTC_Exchange_Orderbook_Bias.poloniex_ask_vol

btc_inst = reddit_crypto.btc
xmr_inst = reddit_crypto.xmr
eth_inst = reddit_crypto.eth
xrp_inst = reddit_crypto.xrp
ltc_inst = reddit_crypto.ltc
dash_inst = reddit_crypto.dash

tradingview_longs = TradingView_Long_vs_Short_Bias.longs
tradingview_shorts = TradingView_Long_vs_Short_Bias.shorts


con = psycopg2.connect( host = 'localhost',
                        database = 'crypto_data_db',
                        user = 'postgres',
                        password = 'postgres')

cur = con.cursor()

cur.execute('INSERT INTO crypto_data (tradingview_longs, tradingview_shorts, coinbasepro_orderbook_bids, coinbasepro_orderbook_asks, binance_orderbook_bids, binance_orderbook_asks, kraken_orderbook_bids, kraken_orderbook_asks, bitrex_orderbook_bids, bitrex_orderbook_asks, poloniex_orderbook_bids, poloniex_orderbook_asks, reddit_inst_btc, reddit_inst_eth, reddit_inst_xmr, reddit_inst_xrp, reddit_inst_ltc, reddit_inst_dash) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (tradingview_longs, tradingview_shorts, coinbasepro_bid_vol, coinbasepro_ask_vol, binance_bid_vol, binance_ask_vol, kraken_bid_vol, kraken_ask_vol, bitrex_bid_vol, bitrex_ask_vol, poloniex_bid_vol, poloniex_ask_vol, btc_inst, eth_inst, xmr_inst, xrp_inst, ltc_inst, dash_inst))    

con.commit()

con.close()