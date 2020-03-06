from bs4 import BeautifulSoup
import requests 
import matplotlib.pyplot as plt




def get_idea_data():

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
        
    3
    ## Data to plot 

    sizes = [longs, shorts]
    colors = ['green', 'red']

    ## Plot 
    plt.pie(sizes, colors = colors,
            autopct = '%1.1f%%', shadow = True, startangle = 90)
    plt.legend([f'{longs} long trade ideas' , f'{shorts} short trade ideas'], bbox_to_anchor=(0,1), loc= 'best', 
                                bbox_transform=plt.gcf().transFigure)


    ## Save plot to staic/images directory
    plt.axis('equal')
    plt.savefig('/Users/julianbaumgartner/Desktop/Python/BTC_Data/static/images/Long_vs_Short.png', bbox_inches = 'tight', trasnparent = True)
