# Happy Cooking Webpage

Third Milestone Project: Data Centric Development - Code Institute

My Happy Cooking Webpage is an interactive webpage, which main purpose is to explore the world through a variety of recipes and to be able to allow the user to discover their passion about cooking. In addition it allows the user to manipulate the data and the recipes, by either crreating, reading, updating and deleting the recipes(CRUD).

## UX

My main purpose when creating the webpage was to ensure that it covers a wide range of recipes from all over the world that can be easily accessed and manipulated.

### User Stories

- As a user of the webpage I want to be able to view all the recipes that the owner of the webpage has provided by clicking a button in the home page.
- As a user I want to specify my search criteria and be able to get results for recipes that fit for vegans and vegeterians.
- As a user of the webpage I want to specify my search criteria and be able to get results for recipes from particular countries.
- As a user of the webpage I want to be able to search for specific recipes by category.(Appetisers, Starters, Main Courses, Desserts).
- As a user of the webpage I want to be able to insert my own recipes and save them to the webpage.
- As a user of the webpage I want to be able to edit the recipes that exist in the webpage by clicking a button and be able to save the updated recipes.
- As a user of the webpage I want to be able to delete the recipes that I do not like.
- As a user of the webpage I want to be able to see all the different categories of the recipes.
- As a user of the webpage I would also like to be able to create, read, update and delete the categories of the recipes.
- As a user of the webpage I want the webpage to have an easy access navigation bar that is clear for the purpose of each section.
- As a user I want to access the webpage from all differend types of divices (MObile Phones, Desktops,Laptops, Tablets, etc.)
- As a user of the webpage I want to be able to insert an image in when inserting or updating a recipe. 

### Wireframes 

![Mobile-Version](static/wireframes/IMG_4847.jpg)
![Desktop-Version](static/wireframes/IMG_4846.jpg)

## Features

- Happy Cooking is a webpage that allows the user to have an easy access and by clicking the "Happy Cooking" logo to always redirect to the home page.
- In the home page there are the recipes together with 3 buttons(View, Edit, Delete) where the user can manipulate the recipes.
- In the home page there are also 3 input fields together with a search button to be able to make the user specify the search by suitability(For Vegans or Vegeterians), country(Italy, Greece, Mexico, Thailand) and catecory(Appetisers, Starters, Main Courses, Desserts).
- There is also a navigation bar, created with [Materialise](https://materializecss.com/navbar.html) with 3 sections on the right top corner (Our Recipes, Add your Recipe, Categories):
1. By clicking "Our Recipes" logo it will always redirect you to the home page where all the recipes are stored.
2. By clicking "Add Your Recipe" logo it will redirect you to the page where you can add your recipe.
3. By clicking "Categories" logo it will redirect you to the page where all the categories are stored and there you can add, edit and delete a category.
- The webpage is also using a slide-out side-navigation bar in order to make it more easy to access by mobile phone [Materialise](https://materializecss.com/mobile.html).

## Features Left to be implemented

In the future i would like to add some links to social media and a registration form for new users.

## Technologies Used

### Front-End

- [HTML](https://en.wikipedia.org/wiki/HTML5) Used for storing all my pages.
- [CSS](https://no.wikipedia.org/wiki/Cascading_Style_Sheets) Used for the styling of my webpage.
- [Javascript](https://no.wikipedia.org/wiki/JavaScript) Used for initialising my buttons and some functions for my recipes.
- [Materialise](https://materializecss.com/) Used for styling of the webpage
- [Material-Icons]( https://material.io/resources/icons/?style=baseline) used for styling my input elements.
- [Jquery](https://en.wikipedia.org/wiki/JQuery) Used for manipulating the dom and add the elements to my project.

### Back-End

- [Flask 1.1.1](https://en.wikipedia.org/wiki/Flask_(web_framework)) A library used for the construction of the webpage
- [Python 3.6.8](https://en.wikipedia.org/wiki/Python_(programming_language)) This is the back-end programming language
- [MongoDB Atlas](https://en.wikipedia.org/wiki/MongoDB) To store all the data and collections of my webpage
- [PyMongo 3.8.0](https://api.mongodb.com/python/current/) MongoDB's API to interact with the data.
- [Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine)) Used for displaying elements from back-end to front0end.
- [BSON ObjectId](https://en.wikipedia.org/wiki/BSON) Used for creating "id's" in the Mongo database.
- [Git](https://en.wikipedia.org/wiki/Git) Used for writting commands and inserting new documents in my webpage
- [Github](https://github.com/) Used to store my webpage for the users to have access to that and for my tutors and mentor to help me with my Milestone Project
- [Heroku](https://en.wikipedia.org/wiki/Heroku) Used for the deployment of my project.

## Testing

- For the potencial users of my webpage that want to be able to see the recipes by clicking a button I have created a view button from Materialise and is triggered in my view_recipe.html with jinja. 

**Add Recipe Functionality:**

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on Add recipe button without filling all the forms | Displays Validation to tell the user to enter all the forms | As Expected | Pass |
| Clicking Add Recipe button after filling all the forms | Redirect to the home page and the recipe is added | As expected | Pass |
| Click on View Button to the recipe that you added | All the information of the recipe display fine | As expected | Pass | 

**Edit Recipe Functionality:**

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on Edit recipe button without filling all the forms | Displays Validation to tell the user to enter all the forms | As Expected | Pass |
| Clicking Edit Recipe button after changing some of the forms | Redirect to the home page and the recipe is edited | As expected | Pass |
| Click on View Button to the recipe that you added | All the information of the recipe display fine | As expected | Pass | 

**Delete Recipe Functionality:**

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on Delete recipe button | Removes the recipe and redirects to the home page | As Expected | Pass |

**Categories CRUD Functionality:**

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on Add Category button without filling all the forms | Displays Validation to tell the user to enter all the forms | As Expected | Pass |
| Clicking Add Category button after filling all the forms | Redirect to the categories page and the category is added | As expected | Pass |
| Click on Edit Category button to a category and press the edit button without filling the forms | Displays Validation to tell the user to enter all the forms | As expected | Pass | 
| Clicking Edit Recipe button after changing some of the forms | Redirect to the categories page and the category is edited | As expected | Pass |
| Clicking Delete Category button | Removes the category and redirects to the categories page | As expected | Pass |

**Filter Functionality:**

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on filter button when choosing vegeterian in suitability | Displays all the recipes that fit for vegeterians | As Expected | Pass |
| Clicking on filter button when choosing vegan in suitability | Displays all the recipes that fit for vegans | As Expected | Pass || Click on Edit Category button to a category and press the edit button without filling the forms | Displays Validation to tell the user to enter all the forms | As expected | Pass | 
| Clicking on filter button when choosing Mexico in country | Displays all the recipes that originated form Mexico | As Expected | Pass |
| Clicking on filter button when choosing Thai in country | Displays all the recipes that originated from Thailand | As Expected | Pass |
| Clicking on filter button when choosing Greece in country | Displays all the recipes that originated from Greece | As Expected | Pass |
| Clicking on filter button when choosing Italy in country | Displays all the recipes that originated from Italy | As Expected | Pass |
| Clicking on filter button when choosing a specific Category in category | Displays all the recipes that refer to this specific category | As Expected | Pass |
| Clicking on filter button when applying multiple filters | Displays all the recipes that fit to the category,country of origin and suitability that are selected | As Expected | Pass |

**Styling of the Webpage:**

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Right click on the webpage and press inspect | The webpage displays fine in all types of devices  | As Expected | Pass |

- The Navigation Bar that the webpage is using is tested for all the types of devices and is working properly.

- The site is tested in a variety of devices such as:Iphones(4 to 10),Samsung Galaxy,Ipads and Desktops.In addition it's tested to all the possible browsers:Chrome, Safari, Internet Explorer, FireFox and i assure that it is compatible and responsive.

The biggest problem I faced when creating this website was how to identify and implement the search functionality, which at the end it was a very interesting feature.

## Deployment

My webpage is hosted in Github and deployed directly from the master branch. The whole project can be viewed here:

[Bumper-Milestone-Project-3](https://github.com/Bumper0417/Milestone-project-3-Python)

In addition my project is deployed in Heroku and the live link can be viewed here: 

[Happy-Cooking](https://happy-cooking-project-3.herokuapp.com/)

The website consists of:
1. A static folder with a css folder,which has a style.css file and a wireframes folder with 2 wireframe images. 
2. A templates folder with 9 html pages.
3. An app.py file where all the backend is stored.
4. A procfile for the deployment in Heroku.
5. A requirements.txt file
6. The README.md file of the webpage.

## Credits

### Content
The content in the whole project is written by me.

### Media 

All the wireframes of the webpage are created by me.

### Acknowledgements

I recieved inspiration from sites such as: 
- [W3schools](https://www.w3schools.com/)
- [Stackflow](https://stackoverflow.com/)
- [Youtube](https://www.youtube.com/watch?v=dTN8cBDEG_Q&feature=youtu.be)
- [MongoDB](https://docs.mongodb.com/manual/text-search/#example)
- [Github](https://github.com/Code-Institute-Submissions/COOK-BOOK-4)
- [Recipes](https://www.bbcgoodfood.com/)

