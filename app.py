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
    return render_template('addrecipe.html',
    categories=mongo.db.categories.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    
    # get the data from the form into a dictionary I can work with
    my_user_data = request.form.to_dict()

    # print the data in the console
    print(my_user_data)

    # my_user_data = {'recipe_name': 'bruschetta',
    #                 'recipe_ingredient': 'this - that - foo - bar'}

    # My "recipe_ingredient" field's value is of data type "string"
    # I want to transform it as a list (array)

    # I get the value :
    recipe_ingredients = my_user_data['recipe_ingredients']          # string
    recipe_ingredients_as_an_array = recipe_ingredients.split(",")  # list (each item is separated by a ",")

    # Update the dictionary key's value :
    my_user_data['recipe_ingredient'] = recipe_ingredients_as_an_array
    
    # Send it to the database: 
    recipes.insert_one(my_user_data)

    return redirect(url_for('get_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
