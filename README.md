# Crypto-Data

### Intro
This program is intended to be a snapshot into the cryptocurrency space. 
Given that it is an ecosystem ripe with volatility and ever changing market structure, 
I believe aggregating different kinds of data into one location, with the time of aggregation being the only constant, 
to be a valuable tool in helping gain insight into the market movements.  
The project uses AWS for a server-less architecture and is hosted on a Linux EC2, running
Gunicorn and Nginx as the web-server. 


### Orderbook Bias
Order-book data was scraped via API’s from a few major cryptocurrency exchanges to help
understand the current flow of capital on the open market. Massive disparities in the order-books 
can signal large shifts in price and investment sentiment. Given that one exchange is only a small portion
of the market, I sourced a few of my favorite exchanges in order to have a broader perspective. 

### TradingView Bias 
TradingView is one of the largest communities of traders openly exchanging ideas and strategies.
You can use the platform to develop strategies, custom indicators, and algorithms that can then 
be back tested against historical data. On the “Ideas” page you can post and view ideas/trades
about any investment or market. Most of these strategies are labeled either long (betting on price going up) 
or short (betting on price going down). This program used Python’s BeautifulSoup module to scrape this 
long vs. short data from the website. The ratio between these two can be a good insight into the current
sentiment of the traders who participate in the market. 

### Reddit Occurrence
Reddit has become the discussion board of the Internet. You can learn, argue, and discuss most any topic on it. 
It hosts a large group of participants in the cryptocurrency community. They are constantly discussing new projects,
developments in existing projects, and the general ups and downs of the market.
This program used the Reddit API wrapper, known as Praw, to scrape the top 300 posts looking
for mentions of certain cryptocurrencies. I believe this is useful data because it shows where the 
interest of the public currently resides. 

### Database 
All values are gathered daily via running the web-scraping programs as a cronjob and are added to an AWS Postgres RDS instance. 
Once this database has a sizable set of data it can be used to find correlations or patterns between upticks 
in order book volume and price or popularity on reddit and on exchange volume ect. 


### API
SAFRS is a python module designed to build REST API’s onto of existing databases and expose them neatly though the swagger UI.
 I modified a few of the scripts to fit my needs. The result is a full access to the postgres database via a dedicated REST API.
