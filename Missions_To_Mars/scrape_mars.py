from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

def scrape():
    executable_path = {'executable_path': 'C:/Users/jenzy/Desktop/Web-Scraping-Challenge/Missions_To_Mars/chromedriver'}
    browser = Browser('chrome', **executable_path)
    
# Mars News
    url= 'https://mars.nasa.gov/news'

    html = browser.html
    soup = bs(html, 'html.parser')

    element = soup.select_one('ul.item_list li.slide')

    title = element.find('div', class_="content_title").get_text()

    paragraph= element.find('div', class_= "rollover_description_inner").get_text()

#JPL Featured Space Image
    jplurl= 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'

    button= browser.find_by_css('button.btn.btn-outline-light')
    html = browser.html
    soup = bs(html, 'html.parser')
    image_url= soup.select_one('div.fancybox-inner img').get('src')
    featured_image_url= f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{image_url}'

#Mars Facts
    url = 'https://space-facts.com/mars/'
    
    tables = pd.read_html(url)
   

#USGS Astrogeology
    base_url = 'https://astrogeology.usgs.gov'
    url = base_url + '/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    html = browser.html
    soup = bs(html, 'html.parser')
    items = soup.find_all('div', class_='item')
    urls = []
    title = []
    html = browser.html
    soup = bs(html, 'html.parser')
    oneurl = base_url+soup.find('img',class_='wide-image')['src']
    img_urls = []
    html = browser.html
    soup = bs(html, 'html.parser')

    oneurl = base_url+soup.find('img',class_='wide-image')['src']
    hemisphere_image_urls = []
    for i in range(len(title)):
        hemisphere_image_urls.append({'title':title[i],'img_url':img_urls[i]})






