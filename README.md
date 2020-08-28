<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">
<h1>Code Institute Milestone Project — 4</h1>

A website designed to allow users to easily browse services,treatments and products available and book a time that suits them should they wish, the business owner benefits by allowing to modify update and change products or services, while also receiving emails with bookings. 

Deployed here - 

<h2>This website can be used for,</h2>

By the customer to view each type service on offer.
By the customer to find out the benefits of each service and what is involved
Allow the customer to pay for the service upfront. Avoiding having the business to always have change available and the customer to remember to bring cash with them on each visit.
Features
The main goal of the homepage / products page of the site is to show the user what services are available and gives them a professional look and clincical feel that fits into what the business is trying to portray. I have included a booking appointment button on the home page so customers can book an appointment easy and receive a call back from the clinic 

The Navbar includes the treatments seperated into non-surgical, dental and products. If the user is logged in then a "Log Out" button is shown, otherwise a "Log In" link is shown. A User must be logged in to proceed to the checkout page, if they are not, and they click they are brought to the Login/ Sign Up page.
Search
The search page returns weighted results utilising PostgreSQL database unique features in django. It searches text, weighting tags as more important and the other sections less important before returning the results. The search uses the same page and view as the home page, just altered to suit the search

The page is broken down into 2 sections, 1)The Login section allows already registered users to sign in using their Username/Email Address and password, if the user was attempting to book an appointment then it will redirect them to the checkout page otherwise it will bring them to the products page. On submitting the details it is checked against what's in the database and if it matches the user is logged in. If the username or password is incorrect the site returns a message explaining why the process was not successful.

<h2>Profile Page</h2>
<h3>Settings<h3>
  <h4>Billing & Shipping</h4>
The main feature of the settings page is to be able to save SHipping and Billing settings seperately, and have them applied seperately. On preparing an order form all fields will be propopulated with the neccessary info. Likewise, all information will be saved to your account if you so choose at payment during the checkout.

<h4>Email & Password</h4>
DJango-allauth has been used for the majority of settings regarding verifivation and security. Most functions work with a redirect to the user's previous oage for a smoother experience However, I found django-allauth to be quite inflexible and obtuse. I would likely not choose it agin.
The checkout app has two sections it allows anonymous checkout and user checkout, in incoporates stripe for secure payments

<h4>The Register section</h4>
Just a button that brings the user to the Register Page and allows the user to add their details. The fields to fill out are kept to a minimum to make sure the user does not feel overwhelmed.

<h4>The forgot password page</h4>
A simple one field form that allows the user to reset their password should they have forgotten it. When clicking the button the user will receive a message to check their email that has been sent, they can then use this to reset their password using a link.

<h2>Future Development</h2>
If I had more time for development I would have included a booking date and time section under the checkout page, it would give the user the available date and times that they can book, this would be taken from a list of events in Google calendar. Each appointment type would have a different calendar in the business. If you clicked a tick appears on the button chosen to confirm this has been picked. When a session in an individual appointment has been booked it would no longer appear in this list of buttons.

<h2>Technologies Used</h2>

<h3>Languages</h3>
<br>Python
<br>Using Django frameworks and other plugins to develop the app
<br>HTML
<br>Page markup
<br>CSS Styling
<br>Javascript
<br>Running functions to initalize components
<br>JQuery
<br>Animations and click functions


<br>Bootstrap4
<br>Used for basic styles and outline

<h3>Resources</h3>
<br>Bootstrap Icons
<br>Used for icons
<br>Google Fonts
<br>Font Styles

Use to resize images for the website 
https://picresize.com/

<h3>Packages</h3>
<br>Please see requirements.txt

<h2>Testing & Troubleshooting</h2>
<h3>Validation</h3>

<p>All forms have validation and will not submit without the proper information.
Links checked with W3C Link Checker
HTML has been validated with W3C HTML5 Validator
CSS has been validated with W3C CSS Validator and auto-prefixed with CSS Autoprefixer. There is a validation issue with margin-block-end but it is a valid value in all popular browser.</p>
<p>Each javascript file was tested on the site for errors and fucntionality using the console and with JSHint
gitignore file has been included to prevent system file commits
requirements.txt updated
Testing</p>

<p>Travis CI is utilised for testing on each branch. If the master branch is tested and passes, the app is automatically deployed to Heroku. THis maintains a functional production app at all times.
Coverage has been utilised throughout the project to ensure all code is tested thoroughly.
A secondary, persistent, PostgreSQL test database has been utilised on Heroku. This way the test database functions more similarly to the production database, with items being added and persisting. THis allows for more accurate testing and test views which function on a real database. Testing must be run with this command to maintain the database's persistence</p>

<br>python manage.py test --keepdb

<p>There is a console log notification that states whether debug mode is off or on.
The views have been thoroughly manually tested and refined over time, utilising python features to create documents in the database in a useful, flexible structure.
The documents in the database have been examined and structured in a manner so that the information is well defined, checking how the views effect documents.
I have tested the site and its layout on multiple android devices, different sizes, on multiple browsers. I was unable to test on iOS. Mainly developed and tested using chrome developer mode. It is fully responsive with a clean layout on each device.</p>
Each feature was developed and tested in its own branch before being pushed to master.
Some tests were performed on views and were tested manually throuroughly. For example, every possible combination on search was tested.
Each time a feature was added all the functions were tested to see if there was an impact.

<h2>Deployment</h2>
Github
Fork the repo on github.
Push the repo to a PaaS, such as Heroku.
Set the environment variables, ensure debug is False.
Deploy and your good to go.

<h2>Credits</h2>
<h3>Content</h3>
Photos are from google images, the project is for educational purpose. The project is based on the codinstitute lessons which was utilised and changed for my needs.

<h2>Awknowledgements</h2>
I'd like to extend a special thanks to all who work and study in Code institute as you've made the process of learning a new skill exciting and working together made the whole process a good bit easier. 
