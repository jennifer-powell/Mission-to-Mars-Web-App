from splinter import Browser
from bs4 import BeautifulSoup as bs
from flask_pymongo import PyMongo
import pandas as pd
import requests

import time
def init_browser():
     
    executable_path = {"executable_path": "C:/Users/jenzy/Desktop/Web-Scraping-Challenge/Missions_To_Mars/chromedriver"}
    return Browser("chrome", **executable_path)
    
    
def scrape():
    
    
    browser = init_browser()
# Mars News
    url= 'https://mars.nasa.gov/news'
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, 'html.parser')
    element = soup.select_one('ul.item_list li.slide')

    title = element.find('div', class_="content_title").get_text()

    paragraph= element.find('div', class_= "rollover_description_inner").get_text()

#JPL Featured Space Image
    jplurl= 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(jplurl)
    # time.sleep(1)
    button= browser.find_by_css('button.btn.btn-outline-light')
    button.click()
    html = browser.html
    soup = bs(html, 'html.parser')
    image_url= soup.select_one('div.fancybox-inner img').get('src')
    featured_image_url= f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{image_url}'

#Mars Facts
    url = 'https://space-facts.com/mars/'
    response = requests.get(url)
    # time.sleep(1)
    soup = bs(response.text, 'html.parser')
    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ['Fact', 'Value']
    df['Fact'] = df['Fact'].str.replace(':', '')
    html_table = df.to_html()

#USGS Astrogeology
    base_url = 'https://astrogeology.usgs.gov'
    url = base_url + '/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    # time.sleep(1)
    html = browser.html
    soup = bs(html, 'html.parser')
    items = soup.find_all('div', class_='item')
    urls = []
    name = []
    for item in items:
        urls.append(base_url + item.find('a')['href'])
        name.append(item.find('h3').text.strip())
    
    browser.visit(urls[0])
    html = browser.html
    soup = bs(html, 'html.parser')
    oneurl = base_url+soup.find('img',class_='wide-image')['src']
    img_urls = []
    for oneurl in urls:
        browser.visit(oneurl)
        html = browser.html
        soup = bs(html, 'html.parser')
        oneurl = base_url+soup.find('img',class_='wide-image')['src']
        img_urls.append(oneurl)
    
    hemisphere_image_urls = []
    for i in range(len(name)):
        hemisphere_image_urls.append({'title':name[i],'img_url':img_urls[i]})




    mars_info = {
        "title": title,
        "paragraph": paragraph,
        "featured_image_url": featured_image_url,
        "html_table": html_table,
        "hemisphere_image_urls": hemisphere_image_urls
        
    }

    browser.quit()

    return mars_info
