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
    #suitability = request.args.get('suitability')
    #country = request.args.get('country')
    #category = request.args.get('category')
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
    recipe_method = my_user_data['recipe_method']
    recipe_method_as_an_array = recipe_method.split(",")
    recipe_ingredients = my_user_data['recipe_ingredients']         # string
    recipe_ingredients_as_an_array = recipe_ingredients.split(",")  # list (each item is separated by a ",")
    recipe_allergens = my_user_data['recipe_allergens']
    recipe_allergens_as_an_array = recipe_allergens.split(",")

    #remove the \r\n from the recipe_method
    recipe_method = [method.replace("\r\n","") for method in recipe_method]

    # Update the dictionary key's value :
    my_user_data['recipe_ingredients'] = recipe_ingredients_as_an_array
    my_user_data['recipe_allergens'] = recipe_allergens_as_an_array
    my_user_data['recipe_method'] = recipe_method_as_an_array

    # Send it to the database: 
    recipes.insert_one(my_user_data)

    return redirect(url_for('get_recipes'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editrecipe.html', recipe=the_recipe, categories=all_categories)

@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    print(request.form.get('is_vegeterian'))
    print(request.form.get('is_vegan'))
    mongo.db.recipes.update({'_id': ObjectId(recipe_id)},
        {
            'recipe_name': request.form.get('recipe_name'),
            'category_name': request.form.get('category_name'),
            'image_url': request.form.get('image_url'),
            'recipe_ingredients': request.form.get('recipe_ingredients'),
            'recipe_method': request.form.get('recipe_method'),
            'recipe_country_of_origin': request.form.get('recipe_country_of_origin'),
            'recipe_vegetarian': request.form.get('is_vegeterian'),
            'recipe_vegan': request.form.get('is_vegan'),
            'recipe_allergens': request.form.get('recipe_allergens'),
            'recipe_nutricion': request.form.get('recipe_nutricion')
        })
    return redirect(url_for('get_recipes'))

#View Recipe
@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    recipes = mongo.db.recipes
    my_recipe = recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('view_recipe.html', recipe=my_recipe)



@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
    categories=mongo.db.categories.find())

@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))

@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name'),
        'image_url':request.form.get('image_url')})
    return redirect(url_for('get_categories'))

@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))

@app.route('/insert_category', methods=['POST'])
def insert_category():
    categories = mongo.db.categories
    category_doc = {'category_name': request.form.get('category_name'),
                    'image_url':request.form.get('image_url')}
    categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))

@app.route('/new_category')
def new_category():
    return render_template('addcategory.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
