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
    - I changed the layout of the cards and changed some values in the media Queries 
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
