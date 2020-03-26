# coding: utf-8
from sqlalchemy import Column, Date, Integer, MetaData, Table, text
from safrs import SAFRSBase

metadata = MetaData()


#def INTEGER(_):
 #   return db.INTEGER
#def DATE(_):
 #   return db.DATE

Base = db.Model
metadata = Base.metadata



class crypto_data(SAFRSBase, Base):
    __tabelname__ = 'crypto_data'

    date = Column(Date, nullable=True, server_default=text("CURRENT_DATE"))
    tradingview_longs = Column(Integer, primary_key=True)
    tradingview_shorts = Column(Integer)
    coinbasepro_orderbook_bids = Column(Integer)
    binance_orderbook_bids = Column(Integer)
    kraken_orderbook_bids = Column(Integer)
    bitrex_orderbook_bids = Column(Integer)
    poloniex_orderbook_bids = Column(Integer)
    coinbasepro_orderbook_asks = Column(Integer)
    binance_orderbook_asks = Column(Integer)
    kraken_orderbook_asks = Column(Integer)
    bitrex_orderbook_asks = Column(Integer)
    poloniex_orderbook_asks = Column(Integer)
    reddit_inst_btc = Column(Integer)
    reddit_inst_eth = Column(Integer)
    reddit_inst_xmr = Column(Integer)
    reddit_inst_xrp = Column(Integer)
    reddit_inst_ltc = Column(Integer)
    reddit_inst_dash = Column(Integer)
    id = Column(Integer)



class Test_table(SAFRSBase, Base):
    __tablename__ = 'test'

    coinbasepro_orderbook_bids = Column((Integer), primary_key=True)
    tradingview_longs = Column(Integer)
    reddit_xmr = Column(Integer)
    posting_date = Column(Date, nullable=False, server_default=text("CURRENT_DATE"))
    
