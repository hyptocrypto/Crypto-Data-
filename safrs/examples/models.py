# coding: utf-8
from sqlalchemy import Column, Date, Integer, MetaData, Table, text
from safrs import SAFRSBase

metadata = MetaData()


def INTEGER(_):
    return db.INTEGER
def DATE(_):
    return db.DATE

Base = db.Model
metadata = Base.metadata



class Crypto_table(SAFRSBase, Base):
    __tabelname__ = 'crypto_data'

    date = Column(DATE(Date), nullable=False, server_default=text("CURRENT_DATE"))
    tradingview_longs = Column(INTEGER(Integer))
    tradingview_shorts = Column(INTEGER(Integer))
    coinbasepro_orderbook_bids = Column(INTEGER(Integer))
    binance_orderbook_bids = Column(INTEGER(Integer))
    kraken_orderbook_bids = Column(INTEGER(Integer))
    bitrex_orderbook_bids = Column(INTEGER(Integer))
    poloniex_orderbook_bids = Column(INTEGER(Integer))
    coinbasepro_orderbook_asks = Column(INTEGER(Integer))
    binance_orderbook_asks = Column(INTEGER(Integer))
    kraken_orderbook_asks = Column(INTEGER(Integer))
    bitrex_orderbook_asks = Column(INTEGER(Integer))
    poloniex_orderbook_asks = Column(INTEGER(Integer))
    reddit_inst_btc = Column(INTEGER(Integer))
    reddit_inst_eth = Column(INTEGER(Integer))
    reddit_inst_xmr = Column(INTEGER(Integer))
    reddit_inst_xrp = Column(INTEGER(Integer))
    reddit_inst_ltc = Column(INTEGER(Integer))
    reddit_inst_dash = Column(INTEGER(Integer))
    id = Column((INTEGER(Integer)), primary_key=True)



class Test_table(SAFRSBase, Base):
    __tablename__ = 'test'

    coinbasepro_orderbook_bids = Column((Integer), primary_key=True)
    tradingview_longs = Column(Integer)
    reddit_xmr = Column(Integer)
    posting_date = Column(Date, nullable=False, server_default=text("CURRENT_DATE"))
    
