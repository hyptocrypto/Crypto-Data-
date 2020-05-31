import random 
import datetime
from locust import HttpUser, task, between


columns = ['tradingview_longs', 'tradingview_shorts', 'coinbasepro_orderbook_bids', 'coinbasepro_orderbook_asks', 'binance_orderbook_bids', 
'binance_orderbook_asks', 'kraken_orderbook_bids', 'kraken_orderbook_asks', 'bitrex_orderbook_bids', 'bitrex_orderbook_asks', 'poloniex_orderbook_bids', 
'poloniex_orderbook_asks', 'reddit_inst_btc', 'reddit_inst_eth', 'reddit_inst_xmr', 'reddit_inst_xrp', 'reddit_inst_ltc', 'reddit_inst_dash']






class Load_tester(HttpUser):
    wait_time = between(5, 9)

    @task
    def index_page(self):
        self.client("/orderbook_bias")
        self.client("/trader_bias")
        self.client("/reddit_posts")

    @task(3)
    def api_call_date(self):
        date=datetime.date((2020), random.randint(4,5), random.randint(1,28))
        self.client('/aip/v1/date/<date>')

    @task(3)
    def api_call_column(self):
        column = random.choice(columns)
        self.client('/api/v1/column/<column>') 