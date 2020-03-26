# Crypto_Data.py

from flask import Flask, request, render_template, url_for


app = Flask(__name__)

@app.route('/')
def orderbook_bias():
    return render_template('orderbook_bias.html')

@app.route('/trader_bias')
def trader_bias():
    return render_template('trader_bias.html')

@app.route('/reddit_posts')
def reddit_posts():
    return render_template('reddit_posts.html')

if __name__ == '__main__':
    app.run()