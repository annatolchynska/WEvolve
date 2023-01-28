# <h1 align ="center"> WEvolve ☯ </h1>
---
[live link is here](https://wevolve-mhc.herokuapp.com/)

 WEvolve is a website of mental healthcare centre that relies on holistic methods and individual, tailor-made treatment programmes as well as classical methods, to restore the balance between body, mind and soul. The centre offers treatments for a variety of mental health issues, such as mental health disorders, eating disorders, depression, panic attacks, PTSD, ADHD, OCD, burnout, personality disorder, addictions and other. Mental and physical health are equally important components of overall health. This site is targeted towards people who are searching for the mental calmness.

---
### Strategy

Project purpose is
* to provide for the user info about mental health issues and treatment providing in the clinic;
* to let user sign up for mental health treatment package;
* to let user book/reschedule/cancel appointment;

### User Experience(UX) and Agile method



### Lucidchart and Data model

<img src="./static/media/erd.jpg">

### Design
The idea of the website and clinic in general revolves around Oriental culture, which represents physical and mental calmness, peace and health. Oriental culture is represented in motivational quotes scattered along the pages.
The font-family is Yeong Sang, that looks like japanese hieroglyphics. All pages has different color palette, but all the colors compliment each other, contrast the backgdound image, are soothing and eye pleasing.

### Future Features
In the future website should have a gallery with the pictures of treatment clinic (resort), the staff and specialists.
The website will provide links and learning material for different coping mechanism related to mental issues (such as meditations, releasing stored traumas through physical activities etc).

### Features
The Landing page has the menu with easy navigation, Sign Up/Sign In buttons. The user isn't able to book an appointment with specialist without having an account and not signed in. It has a logo of the clinic and a motivational quote. 

<img src="./static/media/landingpage.png">

The Navigation bar (menu) on every page looks the same, but presented in different colors to compliment and make a contrast with the background respectively. It is simple and responsive. It has a link to the landing page, represented with the logo and the name of the clinic, contact section with links to the social media, telephone numder and email address, link to the About the clinic page, links to pages that represent different cases of mental issues the clinic treats (such as addiction problems, mental health issues and holistic health phylosophy). There's also link to the page with prices for the treatment. 

<img src="./static/media/menu.png">

The sign up page and sign in page look similar

<img src="./static/media/signup.png">

<img src="./static/media/signin.png">

The contacts page shows the map with the location and all the contact info.

<img src="./static/media/contacts.png">

The About page gives User the obvious glimpse of what the mental health treatment centre WEvolve is. 

<img src="./static/media/aboutpage.png">

The page about mental health issues WEvolve treats has all the info user needs regardless this topic as well as the menu with the opportunity to book an appointment (if the User is authenticated).

<img src="./static/media/mental.png">

The page telling about what the addiction is and how the treatment centre deals with it.

<img src="./static/media/addict.png">

The page that gives a User info about holistic health practices WEvolve implements for mental issues treeatment as well as classic clinical treatment.

<img src="./static/media/hh.png>

The page with prices info
All the pages have the back tag that takes the user to the top of the page.

<img src="./static/media/price.png>

The page with the booking form, where only authenticated User can book an appointment in the clinic.
The form contains all the necessary fields such as first name, last name, email.

The User page where they can manage their appointments (reschedule/cancel).

The page where staff can manage all appointments (reschedule them by demand and cancel as well).

The website has a logo adn it has a footer on the landing and contact pages.

<img src="./static/media/faviconlogo.png">

<img src="./static/media/footer.png">

---

### Technology used:
#### Languages used
* HTML5
* CSS
* JavaScript
* Python

#### Frameworks and libraries used
* Django
* jQuery
* Bootstrap 4
* Google Fonts
* Fontawesome
* Favicon
* Cloudinary  

### Testing

### Bugs and unfixed bugs
While I was early deploying to Heroku, I got an error and the app wasn't working. 

<img src="./static/media/error.jpg">

The issue was that the cloudinary storage wasn't install through the terminal. Then it was installed properly and the app successfully was deployed.

### Deployment
The project was deployed to Heroku using the following steps:

* Create a new Heroku app
* Set the build backs to 'Python' and 'NodeJS' in that order
* Link the Heroku app to the repository
* Push my final code via the terminal after finishing the project.
* Select 'deploy'

#### Elephant SQL
The database was set up by following the steps beneath:

* Log in to ElephantSQL.com to access your dashboard
* Click “Create New Instance”
* Set up your plan
* Select “Select Region”
* Select a data center near you
* Click “Review”
* Check your details are correct and click “Create instance”
* Return to the ElephantSQL dashboard and click on the database instance name for this project
* In the URL section, click the copy icon to copy the database URL
* The proper steps were taken in the settings.py file to connect with the database.

### Credits




