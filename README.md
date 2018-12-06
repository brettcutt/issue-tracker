# Unicorn Bug Tracker
[![Build Status](https://travis-ci.org/brettcutt/issue-tracker.svg?branch=master)](https://travis-ci.org/brettcutt/issue-tracker)

This is the fifth and last milestone project for the Full-Stack software development course through Code Institute. For this project
I followed the project brief. Students are required to build an app offering their own businesses services. This service includes
users being able to create tickets for a bug issue they have, which the company will eventually solve for free and will spend 50% of 
their time working on. The other part of the service is a user can add new tickets for a feature idea, however only the highest paid (upvoted) 
feature will be worked for the other 50% of the companies time. Tickets will be required to have a status showing what stage in development
they're up to and also allow users to comment on individual tickets.

To allow the users to see what sort of progress the company makes on a daily, weekly and monthly basis, some graphs should be shown displaying
those results.

- Heroku app:
  - https://unicorn-bug-tracker.herokuapp.com/

- GitHub repository:
  - https://github.com/brettcutt/issue-tracker
___
## UX

### Strategy
- As a guest, I would not except to have the same priveledges as a registered user.
- As a user I'd expect to be able to register an account, which can be logged into and out of.
- As a user I'd expect to see some sort of description as to what the company does and achieves
- As a user I would expect to be able to add a bug or feature ticket which describes my issue or idea.
- As a user I'd except to see the progress of each ticket by it's status and comments.
- As a user I would expect to be able to upvote a bug ticket, but to keep it fair only once per user.
- As a user, knowing a feature has the be the highest upvoted to be worked on, I'd expect a way to be able to
pay to upvote.
- As a user I would like to know if i've paid for a feature upvote previously before upvoting again. 

### Existing Features
##### User registration and login
- A user can create an account and log into it with their own unique username. 

##### Profile
- A user has their own profile page, where they can see details about their own account. Upon registration
the user is directed here and can visually see a default picture is set which they can change.

##### Header and Footer
- The site name is displayed in the upper left hand corner of the page as a clickable logo that redirects to the home page.
- Navigation buttons are at the upper right hand corner of the page, If admin are logged in an option to go to the admin panel will be avaliable. 
- On mobile the nav menu disappears and a burger menu is there in its place. When clicked the burger icon opens a menu with the navigation buttons.
- A GitHub icon in the footer redirects to my GitHub repository, and other social media icon redirectly to their homepages.

##### Index
- This is the home page featuring a larger title for the whole site.
- There is a short tag line describing that the business can help the user with bugs or features.
- Guests see a register button, where as logged in users see button to the bugs or feature pages.
- A downward arrow at the bottom of the page tells the user they can scroll down or when the arrow is clicked, a jquery smooth
scroll down will trigger.
- Two different sections describe the idea behind bugs and feature. Also graphs shows the progress of bug and feature tickets by
their status and time.

##### Bugs or features
- These pages show a list of the different users bug issues or feature ideas in the form of tickets.
- Each ticket has its own 'view ticket' button that redirect to a page with more detail about that ticket.
- Logged in users have a 'add' button to add a new ticket to the list.

##### Bug or feature detail page
- This is the main page to view more details about a ticket.
- Users are able to comment on the ticket and have that comment displayed on the same page.
- A upvote button allows the user the add one point to the tickets upvotes. A click of a feature ticket upvote button and send
that ticket to the cart, which can later be paid for to add the upvote.
- Each time a user visits a ticket, the view points go up by one.
- If the user is 'admin' or the ticket creator the edit button will show. 
- The ticket status shows what stage that ticket is in.

##### Add or Edit page
- These are the forms to add or edit the tickets.
- If the admin is the one adding or editing the ticket, there will be the option to change the status of that ticket.

##### Cart
- This is where all the pre upvoted feature tickets go.
- The user has the option to remove the ticket.
- There is a summary of tickets being request to be upvoted and the amount it's going to cost.

##### Checkout
- The user can enter and submit their credit card details on this page, to finalize the upvote process.
- Like the cart, a summary of all the tickets being requested is shown.  
___

## Technologies, Libraries and Languages
- **Python**
  - Implement the logic, functionality and responses of the project.
  - https://www.python.org/

- **Django**
  -  A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
  - https://www.djangoproject.com/

- **Jquery was used on the following:**
  - The appearing bugs/ features description and graphs on the homepage.
  - smooth scroll on the homepage.
  - The burger menu on mobile.
  - Pop up buttons on features page.
  - https://jquery.com/
  
- **BootStrap**
  - Made the app responsive on all devices e.g. using "col-xs-12".
  - http://getbootstrap.com/
  - 
- **HTML 5**
  - positioning and format of html elements.

- **CSS 3**
  - Styling the HTML elements.
  
- **Font Awesome**
  - the GitHub icons on the footer.
  - https://fontawesome.com/icons/github?style=brands
  - https://fontawesome.com/license
  
- **Google Font**
  - https://fonts.google.com/

- **Pygal**
  - A python charting library  
  - http://pygal.org/en/stable/documentation/index.html

- **Stripe**
  - Used for the set up and processing of user payments.
  - https://stripe.com/au

- ** Coverage**
  - A reporting tool for python testing.
  - https://coverage.readthedocs.io/en/v4.5.x/

- **WhiteNoise**
  - Allows us to serve our static files on Heroku.
  - http://whitenoise.evans.io/en/stable/
___

### Testing
#### Automated Tests
- You can checkout the automated tests below which all pass. 
- If the repository is cloned, which you can see how to do locally further down this file
, in the terminal type `python manage.py test` to run the automated tests.
Alternatively go the `htmlcov` directory, find the `index.html` file and run it. This will give you a coverage
report of all the tests.

- 1. Accounts
   - [test_Views.py](https://github.com/brettcutt/issue-tracker/blob/master/accounts/test_views.py)
   - [test_Forms.py](https://github.com/brettcutt/issue-tracker/blob/master/accounts/tests_forms.py)
- 2. Bugs
  - [test_Forms.py](https://github.com/brettcutt/issue-tracker/blob/master/bugs/forms.py)
  - [test_Views.py](https://github.com/brettcutt/issue-tracker/blob/master/bugs/test_views.py)
  - [test_models.py](https://github.com/brettcutt/issue-tracker/blob/master/bugs/test_models.py)
- 3. Features
  - [test_Forms.py](https://github.com/brettcutt/issue-tracker/blob/master/features/forms.py)
  - [test_Views.py](https://github.com/brettcutt/issue-tracker/blob/master/features/test_views.py)
  - [test_models.py](https://github.com/brettcutt/issue-tracker/blob/master/features/test_models.py)
- 4. Cart
  - [test_Views.py](https://github.com/brettcutt/issue-tracker/blob/master/cart/test_views.py)
- 5. Checkout
  - [test_Views.py](https://github.com/brettcutt/issue-tracker/blob/master/checkout/test_views.py)
  - [test_models.py](https://github.com/brettcutt/issue-tracker/blob/master/checkout/test_models.py)

#### Manual Testing
- [manual_tests.md](https://github.com/brettcutt/issue-tracker/blob/master/MANUAL_TESTS.md)

##### Responsive
-The project is responsive on all different device modes using Chrome and my own personal mobile.

## project set up

In the terminal command line:
`virtualenv venv`
`source venv/Scripts/activate`
`pip install Django==1.11.15`
`django-admin startproject issuetracker`

settings.py
`ALLOWED_HOST = ['localhost']`

In the terminal command line:
`python manage.py runserver localhost:8000`

## Heroku Deployment
#### Heroku start
- **In heroku**
   - Created a new app and called it `unicorn-bug-tracker`

- **In the terminal command line entered:**
   - `heroku login` Entered username and password.   
   - `git init` to Intilised a git repository.
   - `heroku git:remote -a unicorn-bug-tracker` to link the GitHub repository to the Heroku app.

- **In settings.py:**
  - `ALLOWED_HOSTS=['unicorn-bug-tracker.herokuapp.com']`

#### Setting up the Heroku database
- **In heroku**
  - `Resources`
  - `Add-ons` search `Heroku Postgres` and initiate the `hobby Dev - Free`.
  - `Settings` > `Config Vars` The DATABASE_URL will already be there.

- **In the terminal command line entered:**
  - `pip install dj_database_url`, This allows django to connect to the heroku database url.
  - `pip install psycopg2`, This allows us to connect to the postgres databases.

- **In settings.py:**
  - `import dj_database_url`
  - `DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}`

- **In the terminal command line entered:**
  - A new database requires us to migrate out models again and create a new superuser.
  - `python manage.py migrate`
  - 'python manage.py createsuperuser`

#### Have Heroku host our static files
- **In the terminal command line entered:**
  - `pip install whitenoise`, 

- **In settings.py:**
  - `MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware',]`
  - `STATIC_URL = '/static/'
  - `STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]`
  - `MEDIA_URL = '/media/'`
  - `MEDIA_ROOT = os.path.join(BASE_DIR, 'media')`

- **In urls.py:**
  - `from .settings import MEDIA_ROOT`
  - `urlpatterns = [url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),]`

#### Heroku ConfigVars
- **`Settings` > `Config Vars`**
  - Make sure all the correct variables are stored. 
  - `DATABASE_URL | <your database_url key>`
  - `EMAIL_ADDRESS | <your email address>`
  - `EMAIL_PASSWORD | <your email password>`
  - `SECRET_KEY | <your secret key>`
  - `STRIPE_PUBLISHABLE | <your stripe key>`
  - `STRIPE_SECRET | <your stripe secret key>`
  - `DISABLE_COLLECTSTATIC | 1`

#### Heroku final
- **In the terminal command line entered:**
  - `pip install gunicorn`, this is the package that will run the application on the server.
  - `pip3 freeze --local > requirements.txt` Creates a .txt file which tells Heroku what dependencies the project is using.
  - `echo web: gunicorn.wsgi:application > Procfile` Tells Heroku that this project is a web app and what to run.
  - `git add`
  - `git commit -m 'message'`
  - `git push`

## Running the code locally
- **In the terminal command line enter:**
   - `git clone https://github.com/brettcutt/all-django-projects.git`

   -The dependencies required are as follows or install the ones found in [here](https://github.com/brettcutt/issue-tracker/blob/master/requirements.txt).
     - `pip install Django==1.11.15`
     - `pip install django-forms-bootstrap`
     - `pip install pillow`
     - `pip install django-forms-bootstrap`
     - `pip install pygal`
     - `pip install stripe`


### Media

- laptop background
  - https://pixabay.com/en/home-office-workstation-office-336373/
  - CC0 Creative Commons
  - Free for commercial use 
  - No attribution required

- missing profile picture
   - https://pixabay.com/en/avatar-person-neutral-man-blank-159236/

- Searching daily, weekly and monthly
https://stackoverflow.com/questions/7217811/query-datetime-by-todays-date-in-django 