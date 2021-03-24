# Web-Scraping-Challenge

## Overview
  - To build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 
  

- ## Programs, Languages and Tools
  - Use of: Jupyter Notebook, BeautifulSoup, Pandas, MongoDB, Splinter, Flask, Python, HTML Template

- ## File overview
  - ### Mission_To_Mars.ipynb
    ##### This Jupyter Notebook file scapes the various websites for certain data
    -The lasted news headline from: https://mars.nasa.gov/news
    -Retrieved the featured image from: https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
    -Retrieved facts about Mars from: https://space-facts.com/mars
    -The hemispherre names and pictures from: https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
    
  - ### scrape_mars.py
    ##### This file converts the Jupyter Notebook into a Python script
  - ### app.py
    ##### This file creates a route that will query the Mongo Database and pass the data intoan HTML template to display the data. 
  - ### index.html
    ##### HTML file that takes the Mars data dictionary and display all of the data in the appropriate HTML elements


- ## Steps deployed to reach goal
    - Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs 
    - Used Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.
    - Used Pymongo for CRUD applications for the database. 
    - Used Bootstrap to structure the HTML template.

   ### Mars is a fascinating planet to learn about and explore!

