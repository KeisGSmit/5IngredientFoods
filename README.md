# Your Project's Name

One or two paragraphs providing an overview of your project.

Essentially, this part is your sales pitch.

## Table of contents

<!--ts-->

- [UX](#UX)
  - [High level considerations](#High-level-considerations)
  - [Busniness goals](#Business-goals)
  - [B2B vs B2C](#B2B-vs-B2C)
  - [Strategy Trade-offs](#Strategy-Trade-offs)
  - [Scope plane trade offs](#Scope-plane-trade-offs)
  - [Scope plane requirements](#Scop-plane-requirements)
  - [Scope Plane Requirement types](#Scope-Plane-Requirement-types)
  - [The structure Plane concerns](#The-structure-Plane-concerns)
  - [Interaction design](#Interaction-design)
  - [Information architecture](#Information-architecture)
  - [Architecture types](#Architecture-types)
  - [principles of organisation](#Principles-of-organisation)
  - [The Skeleton plane](#The-Skeleton-plane)
  - [Habits & conventions](#Habits-&-conventions)
  - [Features and usefulness](#Features-and-usefulness)
  - [The Surface Plane](#The-surface-plane)
- [Features](#Features)
- [Technologies Used](#Technologies-Used)
- [Testing](#Testing)
- [Deployment](#Deployment)
- [Credits](#Credits)
<!--te-->

---
 
## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

To deploy this project I followed the following steps:
1. I created my env.py file where I created my variables (IP, Port, MONGo_URI, MONGO_DBNAME and a secret key for flashed massages)
2. I used the CLI to install all my frameworks and collected them inside the requirements.txt file (See requirements.txt)
3. I created my procfile for heroku stating that it should run app.py as a web app and it uses the python language
4. I created my MongoDB and connected to it
5. I went to https://dashboard.heroku.com/apps and created my new app
6. I connected to my GitHub repository via Heroku
7. I then went to setting and added my configuartion variables (same variables as in my env.py file)
8. I connected to my master branch and this is the final step of deployment 

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
