# Crypto_Data.py

from flask import Flask, request, render_template, url_for
import sys
sys.path.append('/Users/julianbaumgartner/Desktop/Python/BTC_Data/BTC_Order_Book_Bias')
sys.path.append('/Users/julianbaumgartner/Desktop/Python/BTC_Data/Long_vs_Short')
sys.path.append('/Users/julianbaumgartner/Desktop/Python/BTC_Data/Reddit_Crypto')
import BTC_Exchange_Orderbook_Bias
import TradingView_Long_vs_Short_Bias
import reddit_crypto


BTC_Exchange_Orderbook_Bias.get_book_data()
TradingView_Long_vs_Short_Bias.get_idea_data()
reddit_crypto.get_post_data()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/trader_bias')
def trader_bias():
    return render_template('trader_bias.html')

@app.route('/reddit_posts')
def reddit_posts():
    return render_template('reddit_posts.html')

@app.route('/test')
def test():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()