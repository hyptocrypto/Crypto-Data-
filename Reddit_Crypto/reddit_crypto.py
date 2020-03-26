''' This program uses the praw reddit API wrapper to scrape 
    the the top 300 post from the CryptoCurrency subredit 
    looking for mentions of Btc, Eth, Xmr, Xrp, Dash and Ltc. 
    Then it uses matplotlib to create a graph comparing the results'''

import praw
import json
import re
import matplotlib.pyplot as plt




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
plt.savefig('/Users/julianbaumgartner/Desktop/Python/BTC_Data/static/images/reddit_postss.png', bbox_inches = 'tight')