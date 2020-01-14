import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGODB_NAME"] = 'happy_cooking'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-3k4ci.mongodb.net/happy_cooking?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)