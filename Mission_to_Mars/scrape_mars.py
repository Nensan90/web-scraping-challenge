import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager 


def scrape():

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
mars_url = 'https://redplanetscience.com/'
news = requests.get(mars_url)
browser.visit(mars_url)

browser.visit(mars_url)
html = browser.html
bsoup = bs(html, 'html.parser')


news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"
featured_image_url = 'https://spaceimages-mars.com/'
browser.visit(featured_image_url)

fact_url = 'https://galaxyfacts-mars.com/'
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(fact_url)
fact_table = browser.html
fact_db = pd.read_html(fact_table, header=0)
fact_df = fact_db[0]

hemis_url = 'https://marshemispheres.com/'
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(hemis_url)
hemis_html = browser.html
hsoup = bs(hemis_html, 'html.parser')

hemis_image_url = 'https://marshemispheres.com/'
browser.visit(hemis_image_url)

dictionary = {'news_title': news_title,
                'featured_img_url': featured_image_url,
                'fact_table': fact_table,
                'hemis_html': hemis_html,
                'hemis_image_url': hemis_image_url}

return dictionary                
