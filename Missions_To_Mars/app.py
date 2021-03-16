# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_info")

# create route that renders index.html template
@app.route("/")
def index():
    mars_info = mongo.db.mars_info.find_one()
    return render_template("index.html", mars_info=mars_info) 

@app.route("/scrape")
def scrape():
    mars_info= mongo.db.mars_info
    mars_info= scrape_mars.scrape()
    mars_info.update({}, mars_info, upsert=True)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)