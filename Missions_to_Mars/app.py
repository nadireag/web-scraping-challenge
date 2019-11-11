from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def home():
    # Find one record of data from the mongo database
    mars_info = mongo.db.mars_collection.find_one()

    # Return template and data
    return render_template("index.html", mars_data=mars_info)

@app.route("/scrape")
def scrape():
    # run the scrape function
    mars_data = scrape_mars.scrape()
    mongo.db.mars_collection.update({}, mars_data, upsert=True)

    # go back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)




