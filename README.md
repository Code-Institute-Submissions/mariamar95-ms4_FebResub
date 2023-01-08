# [Draw with light](https://draw-with-light.herokuapp.com)
This full-stack application was developed for Draw With Light, an online shop where users can view and purchase prints of photographs. The main goal of the website is to display and sell prints to shoppers digitally. 

Draw With Light is a fictional company. It was built with Django, Python, HTML, CSS, JS and. Bootstrap.

![Website on different screens](media/amiresponsive.png)

---

## Table of contents

- [Draw with light](#draw-with-light)
  - [Table of contents](#table-of-contents)
  - [UX Design](#ux-design)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
    - [Database schema](#database-schema)
    - [Style and colours](#style-and-colours)
  - [Features](#features)
    - [Each page of the site shares the following:](#each-page-of-the-site-shares-the-following)
  - [Future Implementations](#future-implementations)
  - [Technologies Used](#technologies-used)
  - [Testing](#testing)
    - [Found bugs](#found-bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Acknowledgements](#acknowledgements)

---

## UX Design

---
### Project Goals

### User Stories

- #### VIEWING & NAVIGATION
  
    | User Story Id 	| As a    	| I want to be able to...         	| So that I can...                                                                     	|
    |---------------	|---------	|---------------------------------	|--------------------------------------------------------------------------------------	|
    | 1             	| Shopper 	| Easily navigate the site        	| Find products and information that I require                                         	|
    | 2             	| Shopper 	| View products by category       	| Find specific items I am interested in without having to scroll through all products 	|
    | 3             	| Shopper 	| View details of each product    	| Learn more about each product                                                        	|
    | 4             	| Shopper 	| View the items I have in my bag 	| Check whether I still wish to purchase the items and amend the quantity if required  	|

- #### REGISTRATION & USER ACCOUNTS
    | User Story ID 	| As a    	| I want to be able to ...                    	| So that I can...                                        	|
    |---------------	|---------	|---------------------------------------------	|---------------------------------------------------------	|
    | 1             	| Shopper 	| Register an account                         	| Have an account with the site and view my profile       	|
    | 2             	| Shopper 	| Receive an email to confirm my registration 	| Verify my account was created successfully              	|
    | 3             	| Shopper 	| Log in and out                              	| Keep my account information secure                      	|
    | 4             	| Shopper 	| View a profile page                         	| Set a default delivery address and view previous orders 	|
    | 5             	| Shopper 	| Reset my password                           	| Recover my account                                      	|

- #### SORTING AND SEARCHING
    | User Story ID 	| As a    	| I want to be able to...                     	| So that I can...                             	|
    |---------------	|---------	|---------------------------------------------	|----------------------------------------------	|
    | 1             	| Shopper 	| Search for a product by name or description 	| Find a specific product I'd like to purchase 	|
    | 2             	| Shopper 	| Find products from a specific category      	| Only see product from that category          	|

- #### PURCHASING & CHECKOUT
    | User Story ID 	| As a    	| I want to be able to...                                    	| So that I can...                                                                        	|
    |---------------	|---------	|------------------------------------------------------------	|-----------------------------------------------------------------------------------------	|
    | 1             	| Shopper 	| Easily select the quantity of a product when purchasing it 	| Ensure I don't accidentally select the wrong product quantity                           	|
    | 2             	| Shopper 	| View all items in my bag                                   	| Make sure I haven't accidentally added the wrong product in my bag                      	|
    | 3             	| Shopper 	| Adjust the quantity of individual items in my bag          	| Easily make changes to my purchase before checkout                                      	|
    | 4             	| Shopper 	| Easily enter my payment information                        	| Check out quickly and with no hassles                                                   	|
    | 5             	| Shopper 	| Save all address info                                      	| I don't have to enter them again on my next order                                       	|
    | 6             	| Shopper 	| View an order confirmation after checkout                  	| Make sure my order was successfully placed and double check that all detail are correct 	|
    | 7             	| Shopper 	| Save all orders on my Profile                              	| Easily access all orders anytime                                                       	|
    | 8             	| Shopper 	| Receive an email confirmation after checking out           	| Keep the confirmation of what I've purchased for my records                             	|

- #### ADMIN & STORE MANAGEMENT
  | User Story ID 	| As a              	| I want to be able to... 	| So that I can...                         	|
  |---------------	|-------------------	|-------------------------	|------------------------------------------	|
  | 1             	| Store Owner/Admin 	| Add a product           	| Add new items to my store                	|
  | 2             	| Store Owner/Admin 	| Edit a product          	| Update product details                   	|
  | 3             	| Store Owner/Admin 	| Delete a product        	| Remove items that are no longer for sale 	|
[Back to top](#Table-of-contents)

---

### Wireframes
- [Home Page](wireframes/wireframe_home.png)
- [Products](wireframes/wireframe_products.png) 

[Back to top](#Table-of-contents)

---

### Database schema
![](documentation/db.png)

[Back to top](#Table-of-contents)

---

### Style and colours
![colour-palette](documentation/colour-palette.png)
After creating the wireframes and main structure of the home page, I needed some inspiration for the style and colour. I sourced an [image](https://www.pexels.com/photo/pile-of-assorted-photos-191429/) that I could use as the background image for the home page. Then I headed to [coolors.co](https://coolors.co/) and use the "create palette from photo" function. I uploaded the image and played around to find a palette I liked.
![create colour palette from background image](documentation/image_picker.png)
I ended up only using the green colours with white to create contrast and make all text easy to read.


[Back to top](#Table-of-contents)

---

## Features

### Each page of the site shares the following:
  -  **Favicon**
     I used [Favivon.io](https://favicon.io/) to create the favicon for the site. I have used the initials of the site to create the favicon and the same font and colours from the site.
      
      ![favicon](static/favicon/favicon-32x32.png)
  -  **Navigation Bar**
      The navigation bar changed based on the size of the screen used.
      ![nav-bar](documentation/nav-bar.png)
      ![mobile nav bar](documentation/nav-bar-mobile.png)

  -  **Footer**  

[Back to top](#Table-of-contents)

---

## Future Implementations
- #### In future implementations I would like to:
  - **Add Wishlist functionality**: Allow users to save all their favorite prints so that it is easier to find them when they revisit the website.
  - **Add user reviews**: Allow users to review products and share photos of how the used the print to decorate their space.
  - **Send newsletters to users**: Give all users the option to sign up to the newsletter and keep them updated on the latest offers.
  - **Allow coupons to be accepted in the checkout**: This is a way to increase sales by offering discounted price to customers. For example offering a discount to a registered user that has not placed any orders to motivate them or reward a repeated customer.
  - **Subscription**: Give users the option to subscribe, paying a monthly fee and getting a free print every month.
  - **Implement Social login/register**: Give users the option to register and login using their social accounts.

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
  ![AWS](documentation/aws-bug.png)

  I deployed the app on Heroku but without the static files. I created a S3 Bucket on AWS to store the static files and linked that to my app. After linking AWS to my app and trying to redeploy on Heroku I was getting the following error:

  ` botocore.exceptions.ClientError: An error occurred (AccessDenied) when calling the PutObject operation: Access Denied
  Error while running '$ python manage.py collectstatic --noinput'. `

  To resolve the issue I have taken the following steps:
    - I checked that the bucket policy had public access.
    - I checked the bucket policy code written in JSON for syntax mistakes.
    - I checked that the AWS Access Key ID and AWS Secret Access Key from where correctly added on Heroku's Config Vars.

  When checking the AWS Access Key ID I noticed that there was a '/' in it which can be problematic. I tried generating a new Access Key ID from AWS and updating it on Heroku's Config Vars which solved the issue.


- #### Stipe Webhook Response Error 
  ![stripe-response error](documentation/stripe-1.png)
  After successfully placing an order, I was getting a 404 response on stripe which meant that the endpoint webhook wasn't found. I found out that it was caused by Gitpod changing the server number of my workspace from eu-80 to eu-81. I updated the endpoint on Stripe and placed another order to test it.
  ![stripe-response error](documentation/stripe-2.png)
  After updating the endpoint I was getting a 400 error. I added some print statements on the webhook file will which raised the following error:
  ![stripe-response error](documentation/stripe-3.png)
  Stripe's Webhook Secret Key wasn't coming through which was causing the problem. That was happening because when I added the Webhook Secret on Heroku's Vars I forgot to added on my env file. When I added the Webhook Secret on the env file I also found that I forgot to add 'DEVELOPMENT' on that file as well. After updating both I placed another order to test it and checked on stipe's webhook logs.
  ![stripe-response error](documentation/stripe-4.png)
  I was getting a 200-OK Response. I committed the changes and tested the deployed app on Heroku as well. After placing an order on the deployed app, I was getting and error again which was caused by a missing trailing slash in the endpoint.
   ![stripe-response error](documentation/stripe-5.png)
  I edited the endpoint on stripe, placed and other order and tested it again.
   ![stripe-response error](documentation/stripe-6.png)


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