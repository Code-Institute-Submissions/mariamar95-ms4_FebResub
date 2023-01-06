# [Draw with light](https://draw-with-light.herokuapp.com)
This full-stack application was developed for Draw With Light, an online shop where users can view and purchase prints of photographs. The main goal of the website is to display and sell prints to shoppers digitally. 

Draw With Light is a fictional company. It was built with Django, Python, HTML, CSS, JS and. Bootstrap.

![Mockup image](Mockup imagelink)

---

## Table of contents

- [Draw with light](#draw-with-light)
  - [Table of contents](#table-of-contents)
  - [UX](#ux)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
    - [Database schema](#database-schema)
    - [Style and colours](#style-and-colours)
  - [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
  - [Technologies Used](#technologies-used)
  - [Testing](#testing)
    - [Found bugs](#found-bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Acknowledgements](#acknowledgements)

---

## UX

---

### User Stories

[Back to top](#Table-of-contents)

---

### Wireframes
- [Home Page](wireframes/wireframe_home.png)
- [Products](wireframes/wireframe_products.png) 

[Back to top](#Table-of-contents)

---

### Database schema

[Back to top](#Table-of-contents)

---

### Style and colours
![colour-palette](documentation/colour-palette.png)
After creating the wireframes and main structure of the home page, I needed some inspiration for the style and colour. I sourced an [image](https://www.pexels.com/photo/pile-of-assorted-photos-191429/) that I could use as the background image for the home page. Then I headed to [coolors.co](https://coolors.co/) and use the "create palette from photo" function. I uploaded the image and played around to find a palette I liked.
![create colour palette from background image](documentation/image_picker.png)


[Back to top](#Table-of-contents)

---

## Features

### Existing Features

- #### Feature1

![Feature1](path here: static/images/homepage.png)

[Back to top](#Table-of-contents)

---

- #### Feature2

![Feature2](path here: static/images/homepage.png)

[Back to top](#Table-of-contents)

---

- #### Feature3

![Feature3](path here: static/images/homepage.png)

[Back to top](#Table-of-contents)

---

### Future Features

- #### Favorite Feature 1

[Back to top](#Table-of-contents)

---

- #### Favorite Feature 2

[Back to top](#Table-of-contents)

---

- #### List of other future features

  - ff1
  - ff2
  - ff3

[Back to top](#Table-of-contents)

---

## Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) - used to structure the web page and its content
- [CSS](https://en.wikipedia.org/wiki/CSS) - used to style HTML files
- [Bootsrap](https://getbootstrap.com/) - used for styling and responsiveness 
- [Django](https://www.djangoproject.com/) - used to simplify development
- [Django-Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) -  used to simplify user authentication, registration, account management
- [Tech3](link to tech) - description

[Back to top](#Table-of-contents)

---

## Testing
  Find more [here](TESTING.md)

### Found bugs

- #### Connecting Django to AWS

  I deployed the app on Heroku but without the static files. I created a S3 Bucket on AWS to store the static files and linked that to my app. After linking AWS to my app and trying to redeploy on Heroku I was getting the following error:

  ` botocore.exceptions.ClientError: An error occurred (AccessDenied) when calling the PutObject operation: Access Denied
  Error while running '$ python manage.py collectstatic --noinput'. `

  To resolve the issue I have taken the following steps:
    - I checked that the bucket policy had public access.
    - I checked the bucket policy code written in JSON for syntax mistakes.
    - I checked that the AWS Access Key ID and AWS Secret Access Key from where correctly added on Heroku's Config Vars.
  
  When checking the AWS Access Key ID I noticed that there was a '/' in it which can be problematic. I tried generating a new Access Key ID from AWS and updating it on Heroku's Config Vars which solved the issue.

![AWS](documentation/aws-bug.png)

- #### bug2

![bug2](img/bug2)

- #### bug3

![bug1](img/bug3)

---

## Deployment

[Back to top](#Table-of-contents)

---

## Credits
- ### Code
  - Boutique Ado walk-through project from [Code Institute](https://codeinstitute.net/)
  - [Bootstrap Docs](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
  - [Django-Allauth Documentation](https://django-allauth.readthedocs.io/en/latest/installation.html)

### Content
- Hero Image By [Pineapple Supply Co](https://www.pexels.com/photo/pile-of-assorted-photos-191429/)

### Acknowledgements

[Back to top](#Table-of-contents)