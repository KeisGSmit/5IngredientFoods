# Your Project's Name

5 Minute Foods was intiallly a Pokédex for "Pokémon Go" but was remastered to be a site, where people can share recipes.
5 Minute Foods was inspired by the heaps of hand written recipes in my parents' kitchen. My mom would always try and find recipes from relatives, some recipes did not
exist on paper. So to make finding and sharing recipes easier, 5 Minute Foods was born. The name originates from my laziness; I would not spend more than 5 minutes
looking and sharing recipes. 

## Table of contents

<!--table start-->

- [UX](#UX)
    - [Strategy Plane](#Strategy-plane)
    - [Scope Plane](#Scope-Plane)
    - [Structure Plane](#Structure-Plane)
    - [Skeleton Plane](#Skeleton-Plane)
    - [Surface Plane](#Surface-Plane)
- [Features](#Features)
- [Technologies Used](#Technologies-Used)
- [Testing](#Testing)
- [Deployment](#Deployment)
- [Credits](#Credits)
<!--table end-->

![Mock-up](Readme_sourceFiles/mockup.png)
---
 
# UX
## Strategy Plane
### High level considerations
-	Looking at the target audience: This is a very culturally appropriate project. 
It is a web app that focuses on sharing recipes. 
-	Anybody can use this web app. The content will focus on recipes and food. 
-	We can track and catalogue the content in an intuitive way by using forms and databases
-	The content will be entered into a database and be displayed to the different pages
-	Cook books require people to buy the books while this web app provides the recipes for free
-	The technology we are using is very modern: HTML5, CSS3, JavaScript, Python and MongoDB

### Business goals 

Due to the assessment, business goals are negligible. 

### Trade Off 


-	I am making a Web app that allows people to find and share recipes  
-	The value we provide is to be able to quickly find recipes and share them. 
-	Anyone is allowed to use the website (Due to this I am reluctant to use a login system)
-	People looking for recipes are people who do not know what to make for breakfast/dinner/lunch so we aim to provide as many recipes for these as possible. 
-	Competitors normally share their recipes in a blog which makes it tedious because as a user, we do not care about the blogger’s life story regarding that recipe,
 we just want the recipe. 
-	Competitors who share their recipes on non-blog sites normally share gifs of their recipe on forums (Reddit) but without knowing that you can control the gif
 makes it long to find the next step because you will have to wait for the gif to replay before you can see the next step. 
-	User needs: 
    - Easily find and share recipes 
-	Site owner’s goal:
    - Promote cooking equipment (AMC Classic (?)) (Maybe)
-	Will need to have minimum features for single use learning


![The Features diagram](Readme_sourceFiles/tradeOff.png)


### The trade off

- I have rated each feature from 1 - 5 (where 1 is the least and 5 is the most) on importance and viability

- First I add up the total on importance, which is 33

- Then I find my average viability, which is 4.25. Then I multiply that by the 
number of items, which is 34. 

- My importance "value" is 33 and my viability is 34. Thus viability > importance
    - this means that all features can be implemented

- Depending on the time constraints the items with the lowest importance will be incorporated last
## Scope Plane

### Trade off

- The features that are open for discussion at the moment (16/11/2020) (DD/MM/YYYY) is the Promotion of Products and the comment section 
on each recipe because they have the lowest viability of all the features

- the project should be done within 3 weeks 
    - I have 21 days to implement 8 features
    - This means one feature should be implemented every +-3 days  

##### comments

- an issue with the comment section is:
    - if there is no login system (as stated above) all comments will just appear as paragraphs and will not
    satisfy the first time learning and lead to a bad UX. 
    - if there is a login system then further research will have to be done to be
     able to incorporate a voting system to rate the most helpful comments and
      to permanently show each comment to the correct url. 
        - this leads to another issue: how do I prevent a user voting more than once?
        - another issue is that many users using the app are just visitors and will not want to sign up to this system
    - This means another database needs to be established.

- Thus, I believe the comment section should not be included. 

#### Promotion of products

- This seems more viable than the comment section 
- A local Json file can be established with images, names and links 
of certain cooking equipment used in the different recipes and these can be
 used to promote products. (Linking user to the Official product site)

### Requirements
- I conducted an interview with my family regarding this section asking them 3 main questions
    - what do the users say they need?
        -  One User wanted a conversion Table
            - this can be incorporated under each recipe's individual page 
        - One user wants media - photos/gifs of the recipe
            - this can also be incorporated in each recipe's individual page
        - Users said they wanted a difficulty level for each recipe
            - I found this to be relative to each person and can lead to intimidation - Thus bad User experience
        - One user said they wanted cooking tips at the side but this is so niche to each recipe
            - This was not included
        - Another user wanted the recipes to already be on the app but this defeat the purpose of the goal: to be able to share recipes
            - This will have to be done to make the project seem completed
        - Users want to know if the recipe was tested by different users
            - This will rely on a comment section, which will not be included
        - Users wanted categories for each recipe
            - main course, sides, desserts etc...
            - There has to be a limit of categories
                - that means once the category is created, it stays there. No admin control would exist
        - Users wanted cooking "teachings" to teach people using the app how to cooking
            - But this misses the site's goal and can be considered negligible 
        - Users wanted a filtering system to be able to filter their searches by difficulty
            - this can be done by creating an index in mongoDB 
            - Instead a search feature was added to be able to search for recipes by name
    - what they actually need 
        - Users were unaware of the requirements:
            - to have a responsive design 
            - to have a navigation system
        - users wanted to share the recipes via pictures but this going to lead to recipes being misread and/or misunderstood
    - what they do not know they need
        - The submission form here is crucial since this is the only logical way to get the recipe online in a clear and comprehensive manner.
        - Users were unaware of the importance of the wireframes and the surface plane.

### Requirement types

- Looking at the content requirements there will be a lot of mixed content of the multiple pages
    - Images/ gifs, Cards, Ordered and Unordered lists with a lot of text

- considering the viability of the scope plane requirements I would say that the requirements 
we can include (outside of the initial features) are:
    - The conversion Table
    - media/ gifs of the recipe
    - The categories for when the meal is applicable (dinner/lunch/breakfast etc.). these will be stored in a database and they will be part of a drop down list in the submission form
    - The filtering system/search functionality 
- the requirements can't include due to viability is:
    - The difficulty level
        - I support this idea but difficulty is relevant: Gordon Ramsey might find roast beef simple but a 15 year old could find it challenging/dangerous
    - The cooking tips
        - I can attempt to include this but if it makes the database full then it will probably not be included
    - The comment section as disscussed


- The requirements listed are not features but they are "nice to haves"
- Incorporating them could round off this project quite nicely and make the projects seem more useful, buildable, objective and functional

- A non-functional requirement I am seeing is scalability 
    - I will have to move to a better, larger server if the traffic gets too big
        - this means setting up new environment variables which can be done but will definitely cost money

## Structure Plane
### Concerns

- The following diagram displays how I plan to organize the functionality & content 
of the site and how a user might navigate through the site intuitively 

![Structure plane](Readme_sourceFiles/Structure_plane.png)

- The user will start at the landing page 
- At the top will be a nav bar with 5 sections: Share, Find, About, appliances and Home
    - "Share" will be a submission form
    - "Find" will be a gallery/catalogue with a filter that uses advanced routing
     to direct a user to an individual recipe, where the user can edit or delete a recipe
    - "About" will give a bit more information on the project's background
    - "Appliances" will be a gallery of appliances from a Json file that links a user to the official site of that appliance
    - "Home" will take a user to the landing page

- The plan is to have a linear hyperlinked structure that is simple enough
 for users to navigate through but complex enough to include a lot of information


### Interaction design 

- Firstly looking at how the databases and collections are going to be set up: I have designed a rough sketch in my head 
![Data base design](Readme_sourceFiles/DBDesign.png)
- The Recipe collection will be the "main" database where each entry will have attributes:
    - Category_name: This will "categorise" the recipes for the corresponding meal times
    - type: The will also categorise the recipes but for what type of dish it is.
    - Name: will be the name of the recipe, the search functionality will target this attribute
    - instructions and ingredient: these two fields will be in the form of an array of strings. By using Java Script 
    I plan to create more input fields in the form. For each input field (for the two attributes), that will get pushed into the corresponding array to MongoDB. 
        - To get this to appear on the recipe's page, I will filter through each item in the array displaying the ingredients in an `<li></li>` child of 
    an `<ul></ul>` and the instructions in an `<li></li>` that is a child of an `<ol></ol>`
    - Img: this will be a url of a gif or a image of the meal 
    - Finally each database will have a Primary key auto generated by MongoDB called "_id"

![ERS Diagram of the database](Readme_sourceFiles/ERS_diagram.png)
This is my attempt at trying to draw an ERS diagram of the database's collections


- Looking at the interactive systems discussed so far:
    - The gallery/catalogue of recipe cards to click on
        - each recipe will be in a card which when clicked on will take you to that recipe's page
        - there will be a search bar above all the cards that allows the users to search for recipe names
    - The submission form to submit recipes
        - there are input fields to enter data 
        - if more ingredients/instructions need to be added there will be a button that "reveals"/"adds" more input fields
        - on submission the form's data will get pushed to the database where the recipe will be on display in the "Find" section
    - The appliance page to promote appliances for the page owner
        - This will be a simple gallery that will send a user to the site selling that appliances

- The landing page will contain a form that allows people to send messages to the site owner, if any problems arrive
    - This is to add a better UX so that correspondance between user and owner can be made efficent. 

- The Site will try to Leverage from Prior experience by assuming the user has an expectation of convention
    - Like having the Nav Bar at the top of the page

- The Theme of the page will be consistent 

- By using a Library like materialize the voice of the site will remain consistent and stable

- Due to the simplicity of the structure of the site, the app/site should be very learnable

### information Architecture

- This section is responsible for the creation of organisation and navigational schemes which has already been discussed in the structure plane concerns and 
the interaction design. 

- the architecture, I believe, is done correctly so that when changes are made the architecture can accommodate those changes

- The architecture forms a Tree Structure which is relatively standard
    - This is known to be problematic on Mobile but with the ease of a burger icon, I plan to reduce those problems

### Principals of organisation

- The way data will be organised as follows:
    - The organising principles used at the highest levels of the site should be most
    closely tied to user needs & business objectives
        - that means a link to share/find a recipe should be in the navigation bar
        - The link to promote cooking appliances should also be in the Nav
    - Organising rules at lower levels are influenced by future specs & content requirements
        - Like the comment section 

## Skeleton Plane

Here Are the wireframes of the site for different modern devices 
- [Desktop view](Readme_sourceFiles/DesktopWireframe.pdf)

- [Mobile & Tablet view](Readme_sourceFiles/MobileAndTabletView.pdf)

## Surface Plane

To add Visual language to the site, here are the design choices I made.

- This is the designated colour pallet 
![Colour pallet for the site](Readme_sourceFiles/pallet.png)

- The font family will remain consistant and will be the standard materialize font.

- Regarding images:
    - images in the cards of the "appliances" and "find" section must be contained and square

- Each section of the site will have a cover photo while the landing page has a carousel but the images in the carousel need to be the same
as the images in the cover photo

# Features
 
## Existing Features
- Form on landing page 
    - Allows users to contact the site owner, by having them fill out a form
- Sharing recipes 
    - Users can share recipes by filling out the form on the "share" section
- Finding recipes
    - Users are able to scroll through the cards on the "find" section 
    - Users can search for recipe names in the search bar at the top of the "find" section 
- Updating recipes
    - Clicking on a individual recipes link and scrolling down will expose the update button
    - Clicking on that button collects all previously entered data in the "share form" and allows a user to modify anything they like
    - Clicking on submit will update that recipe
- Deleting a recipe
    - Clicking on a individual recipes link and scrolling down will expose the delete button 
    - Clicking on that button activates a modal for defensive programming 
    - Clicking on Cancel closes the modal 
    - Clicking on delete deletes that recipe. 
- Appliances Promotion
    - In the "appliances" section there are cards with different applainces
    - Clicking on the individual links takes a user to the official site where that appliance will be sold.


## Features Left to Implement
- I want to incorporate pagination in the "find" section
- I want to advance my search bar's abilities by adding more indexing in the recipes collection
- I want to add a comment section under each recipe's individual page

# Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

## Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets#CSS_3)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Pyhton3](https://www.python.org/downloads/release/python-380/)

### Tools

- [Autoprefixer](https://autoprefixer.github.io/)
- [Markup Validation service](https://validator.w3.org/)
- [GitHub](https://github.com/)
- [Git](https://git-scm.com/)
- [Gitpod](https://chrome.google.com/webstore/detail/gitpod-online-ide/dodmmooeoklaejobgleioelladacbeki?hl=en)
- [VSC](https://code.visualstudio.com/download)
- [Microsoft Office](https://www.office.com/)
- [favicon](https://www.favicon.cc/)
- [JSHint](https://jshint.com/)

### Frameworks

- [Materialize](https://materializecss.com/)
- [Font Awesome icons](https://fontawesome.com/icons?d=gallery)

The following are frameworks imported from the cheese shop (They can be found in requirements.txt). 
- [Flask](https://pypi.org/project/Flask/)
- [PyMongo](https://pypi.org/project/pymongo/)
- [Click](https://pypi.org/project/click/)
- [DNSPython](https://pypi.org/project/dnspython/)
- [Flask-PyMongo](https://pypi.org/project/Flask-PyMongo/)
- [itsdangerous](https://pypi.org/project/itsdangerous/)
- [Werkzeug](https://pypi.org/project/Werkzeug/)

### libraries

- [JQuery](https://jquery.com)



# Testing

1. Testing if Project deploys successfully to Heroku: (Sha: 937c8b93b29328c060febef617a9b8f7421e3a7d)
    - after the [Deployment](#deployment) sequence I pushed my work to GitHub
    - I got a jinja error
    - I revisited my app.py file and saw I rendered the wrong template which does not exists
    - To fix this I renamed the template to the correct corresponding template which does exists (sha: 079dc6719fb3d9ca5ac7e4859456d2a042d8becd)
    - app now successfully launches to Heroku. 

2. Testing if CSS and JS files are successfully connected to the base.html
    - In the base.html I linked Jquery, my CSS file(static/css/style.css using Jinja) and my JavaScript file (static/js/main.js using Jinja)
    - I changed the font colour in the CSS file and the h1 font changed - Thus successful 
    - I added a button to base.html and added Jquery code to my JavaScript file that will change the background colour and the font colour 
        - on click the button changed color and background color - Thus successful
    - My CSS file and JavaScript files are successfully connected

3. Testing the "responsive" images of cards in applainces.html
    - I first set all images to have dimesnions 100px X 100 px
    - Not all devices supported these dimesnions
    - I added media queries in style.css to chnage dimensions of the images appropriately 
    - Due to the layout It was not successful 
    - I changed the layout of the cards and chnaged some values in the media Queries 
    - Cards now Successfully show the images and are appropriate for the following devices (in portrait and Landacape):
        - laptops
        - Moto G4
        - Galaxy S5
        - Pixel 2/2XL
        - IPhone 5/SE/6/7/8/8 Plus/X
        - IPad & IPad Pro
        - Surface duo 
        - Galaxy Fold 

4. Testing if form submits recipe to MongoDB
    - I filled the form with test data and added "extra" data to instructions and ingredients (To test if an array will store the different instructions and ingredients)
    - Form does not submit to MongoDB
    - I added a different collection as the target for the insert function
        - this did not work 
    - I added a method and a action to the form 
        - The form submits the data to the wrong collection
    - I changed the collection back to the orignal target for the insert function
    - Form now submits correct data to the right collection 

5. Rendering recipe.html 
    - I added the corresponding app route and Jinja returned a TypeError saything that I can not iterate over the object
    - I removed the Jinja for loop and my page rendered but the injected data does not show up
    - I changed the collection from recipe to recipes in the route 
    - data from the collection now renders to recipe.html successfully 

6. Getting the update button to load data on the update.html page
    - In recipe.html I added a update button which parses a varibale (Recipe ID) to app.py
    - I created a app route and function in app.py that renders update.html and takes the parsed variable as a parameter
    - I tried to look for the recipe ID and got a `bson.errors.InvalidId error: 'recipe' is not a valid ObjectId, it must be a 12-byte input or a 24-character hex string`
    - I renamed variables in the HTML file and I renamed variables in the python file so that the word recipe does not appear in the error but it still does.
    - A soon as I restarted the app the error was gone and my page loaded successfully

7. Testing if Updating a Recipe works
    - I am using the "Test" Recipe 
    - I will change the name to "Test2" and click on update 
    - A new recipe was created
    - I went back to the update submission form and changed the action from `action="{{ url_for('share') }}"` to `action="{{ url_for('update') }}"`
    - I went back to MongoDB and removed Test2
    - I am going to open up the test recipe again in find.html and I will attempt to update it's name to "test2"
    - I got a Jinja error, I changed `return redirect(find.html)` I coppied and pasted code from the view of `find()` into my function
    - After updating a User is taken to the `find.html` page.

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well.
 Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, 
 with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach,
 link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant.
 A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

# Deployment

Link to the live page: https://keis5ingredientsfoods.herokuapp.com/ 

To deploy this project online I followed the following steps:
1. I created my env.py file where I created my variables (IP, Port, MONGo_URI, MONGO_DBNAME and a secret key for flashed massages)
2. I used the CLI to install all my frameworks and collected them inside the requirements.txt file (See requirements.txt)
3. I created my procfile for heroku stating that it should run app.py as a web app and it uses the python language
4. I created my MongoDB, populated it with data and connected to it
5. I went to https://dashboard.heroku.com/apps and created my new app
6. I connected to my GitHub repository via Heroku
7. I then went to settings and added my configuration variables (same variables as in my env.py file - see image below)
![Conviguration variables](Readme_sourceFiles/configVars.png)

If you do not understand the code above: 
    - IP is 0.0.0.0
    - PORT is 5000
    - MONGo_URI is mongodb+srv://Root:`<my password>`@myfirstcluster.kbel5.mongodb.net/`<my database name>`?retryWrites=true&w=majority
    - MONGO_DBNAME is food
    - SECRET KEY is a password
8. I connected to my master branch and this is where commits to the master branch will be deployed to the live project

To deploy this project offline/locally I followed the following steps:
1. 

# Credits

## Content
- The text for section Y was my own

## Media
- The colour scheme was created by me, Inspired by [this arcticle](https://www.quora.com/What-color-scheme-to-choose-for-food-website) but I used [Palleton](https://paletton.com/#uid=1000u0kllllaFw0g0qFqFg0w0aF)
- The images for the site was obtained from [Unspalsh](https://unsplash.com/)
- The conversion table in recipe.html can be found [here](https://sugarandcharm.com/charming-printable-kitchen-conversion-chart)
## Acknowledgements

- I was able to dynamically add content fields and recieved inspiration from [Sanwebe](https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery)
- To be able to add the instructions and ingredients as an array to my collection in MongoDB, [Miklos](https://github.com/Sarosim) helpped me
- [Igor](https://github.com/bravoalpha79) assisted me in being able to get data to show up in recipe.html 
- My family were the users who were interviewed 
- [How to dynamically add html elements](//https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery) for my Jquery in my JavaScript file 