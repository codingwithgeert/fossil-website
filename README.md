<div align="center"><h1>The Fossil Shop<h1></div>

<div align="center">
<img src="https://i.ibb.co/x6SqLj1/fossilshop.png" alt="fossilshop" border="0" width=30% height=30%>
</div>
<br>
This webpage is a ecommerce webshop. It is made with Django. Customers can buy fossils and put them in a cart.
When they login they can see their cart history and order details.
After paid by Stripe there is an email sent with the user with their order detail.

The link to live page: [The Fossil Shop](https://the-fossil-shop.herokuapp.com/ )


## UX
 
#### User Stories
- As a customer I want to search on the webpage for the item I want.

- As a customer I want to be able to create my own account to login on the webpage.

- As a customer I want to have my items i clicked stored in a cart.

- As a customer I want to see a detailed page of the item i clicked.

- As a customer I want to have a form to contact the admin of the website.

#### Design

The logo of the website is at the top left. Next to it are the navigation links you can interact with by clicking on them.
On mobile devices the navigation links are inside a hamburger icon.
When the user comes on the site it will see a carousel with pictures.
Beneath it is the webshop name and a slogan.
In the footer are some quick links the user can click which brings them to other pages.

#### Wireframes

- [Desktop Homepage](https://i.ibb.co/0XVnd0m/Desktop-Wireframe-Home.png)
- [Desktop Productpage](https://i.ibb.co/1XrctyT/Desktop-Wireframe-Fossils-page.png)
- [Mobile Homepage](https://i.ibb.co/1dbq2Tx/Mobile-wireframe-Home.png)
- [Mobile Productpage](https://i.ibb.co/G0XnRW0/Mobile-wireframe-Fossils.png)


## Features

- <u>Stripe pay button:</u> A button to let the customer click on that opens up a payment window.
- <u>Search bar:</u> Allow users to search for items in the webshop.
- <u>Detailed page:</u> A link to the detailedpage where the user can see info about the product.
- <u>Add to Cart button:</u> The user can click on this button and as an result it will be stored inside their cart.
- <u>Email:</u> is send to the customers email used in the payment form.

#### Features Left to Implement
- Bidding System
- Message to be send to webshop owner by using an form.
  

## Technologies Used

#### Tools:

- [AWS Cloud9](https://aws.amazon.com/cloud9/) used for their IDE while building and testing the website.
- [Balsamiq](https://balsamiq.com/) used for the wireframes/mockups.
- [Django](https://www.djangoproject.com/) uses as framework.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) Rendering of all the forms on the website.
- [GitHub](https://github.com/) to store and share all project code to the github site.
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) for the version control.
- [Gunicorn](https://gunicorn.org/) Python WSGI HTTP Server for UNIX.
- [Heroku](https://www.heroku.com/) for application deployment.
- [Imgbb](https://imgbb.com) to upload all external images.
- PIP is used to download all the tools in the requirements.txt
- [Psycopg2](https://pypi.org/project/psycopg2/) PostgreSQL database adapter.
- [Pillow](https://pillow.readthedocs.io/en/stable/) Python imagin library.
- [Stripe](https://dashboard.stripe.com/register) for the online payment option on the website.
- [Travis](https://travis-ci.org/) testing tool
- [Whitenoise](http://whitenoise.evans.io/en/stable/) for static files
-[Django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks) used for form tweaks. 

#### Database:

- [PostgressSQL](https://www.postgresql.org/) powerful, open source object-relational database
- [SQLite3](https://www.sqlite.org/index.html) a small and fast library used for testing.

#### Programming Languages:
- This project is programmed in: Python, css, and html 

#### Libraries

- [Bootstrap 4](https://https://getbootstrap.com/) as a framework.
- [Font Awesome](https://fontawesome.com/) for the icons used on this website.
- [Google Fonts](https://fonts.google.com/) for website fonts styles.
- [JQuery](https://jquery.com) for DOM manipulation.


 


## Testing

#### Manual testing: 

All steps on desktop were repeated in browsers: Firefox, Chrome and Internet Explorer 

##### 1. search on the webpage for the item you are looking for:

 Mobile and tablet:
1. Make sure you are on the index.html page.
2. Beneath the second header you will see a searchbar with the text: "Search for products".
3. When you type in ammonite. All the products with this name will show.
4. If not then the item is not in the store.

 Desktop:
1. Make sure you are on the index.html page.
2. Beneath the second header you will see a searchbar with the text: "Search for products"
3. When you type in sharktooth. All the products with this name will show.
4. If not then the item is not in the store.

##### 2. Create you own account.
 
 Mobile and tablet:
1. This can be done on any of the pages.
2. Click on the hamburger icon in the top left of the screen.
3. A menu pops up with all the links to each page.
4. Click on the sign up link.
5. This will bring you to a different page.
6. Fill in the form. And when done click the sign up button.
7. Well done your account is now created!

 Desktop:
1. See step 1 one above: Click on the sign up link.
2. This will bring you to a different page.
3. Fill in the form. When done click the sign up button.
4. Well done your account is now created!

#### 2. Get your items in your cart.

 Mobile and tablet:
1. You first have to be logged in as without an account you cant add an item to your cart.
2. Now make sure you are on the index.html page.
3. Beneath the search bar you see the shop items.
4. Click on the blue add to cart button for which item you want to be added.
5. If you done it right a number appeared next to the cart icon at the top of the page.
6. For example: if you pressed two of the buttons twice it should show a (2)

 Desktop:
1. This can be done on any of the pages.
2. You first have to be logged in as without an account you cant add an item to your cart.
3. Now make sure you are on the index.html page.
2. Beneath the search bar you see the shop items.
3. Click on the blue add to cart button for whivh item you want to be added.
4. If you done it right a number appeared next to the cart icon at the top of the page.
5. For example: You pressed the button three times it should show a (3)

#### 3. Go to the detailed view page

 Mobile and tablet and desktop:
1. You have to be on the index.html page
2. Scroll down and you will see the different items in the store.
3. Click on the name of one of the items.
4. After you done this a new page comes up.
5. Here you can see all the details of the product you clicked on.

#### 4. Fill in the form to contact the admin of the webshop.

 Mobile and tablet and desktop:
1. This can be done on any of the pages.
2. Scroll down to the footer of the page.
3. Click on the link: Contact Us.
4. You will go to a different page.
5. Here you can fill in the form.
6. When done click on the submit button.
7. After you clicked the button a thank you message appears

 

#### 5. Github icon in the footer brings you to github homepage in new window.

 Mobile, tablet and desktop:
1. This can be done on any of the pages.
2. Go down the page untill you can see the footer.
3. There you see the text: "Website built by: Geert van Kaathoven." 
4. Next to it is an green icon.
5. This is the github icon you need.
6. click on this icon.
7. a new tab opens up to the creator of this websites github.

#### Automatic test:

#### Bugs
- The form at the contac us page is not working. Instead it does show an: 
"Your message has been sent to the user" page.(see features left to implement)

## Deployment
This project was developed using the [AWS Cloud9 IDE](https://aws.amazon.com/cloud9/?origin=c9io), committed to git and pushed to GitHub using the built in function within cloud9.

To deploy this project to GitHub Pages from its GitHub repository, the following steps were done:

1. Log into GitHub account.
2. From the list of repositories on the screen, select Errepulify/Repositories/wildlife-globe-explorer
3. From the menu items near the top of the page, select Settings.
4. Scroll down to the GitHub Pages section.
5. Under Source click the drop-down menu labelled None and select Master Branch
6. On selecting Master Branch the page is automatically refreshed, the repository is now ready to be deployed.
7. Scroll back down to the GitHub Pages section to retrieve the link to the deployed website.

#### How to run this project locally

To clone this project from GitHub:
1. Follow this link to the [GitHub repository](https://github.com/Errepulify/fossil-website)
2. Under the repository name, click "Clone or download".
3. In the Clone with HTTPs section, copy the clone URL for the repository. 
4. In your local IDE open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type ```git clone```, and then paste the URL you copied in Step 3.
```console
git clone https://github.com/USERNAME/REPOSITORY
```
7. Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub [here](https://help.github.com/en/articles/cloning-a-repository).

#### Heroku Deployment

To deploy Wildlife Globe Explorer to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
 --- | ---
DATABASE_URL | `postgres:your databaselink`
SECRET_KEY | `<your_secret_key>`
STRIPE_PUBLISHABLE | `Your own stripe pk key here`
STRIPE_SECRET | `Your own stripe secret key here` 

8. In the heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed.


## Media

- The icons are from font awesome.
- Picture used in the about us page is from: [unsplash](https://images.unsplash.com/photo-1555602015-9efbc925fc5d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=600&q=60)

## Code

- Testing code is from [Unittest](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn)
- Used the udemy video Build Ecommerce Website to Master Django and Python as reference.
- The email template sent to user is from udemy video Build Ecoommerce Webiste to Master Django and Python.
- The videos from Code institute.
- Card code is from official bootstrap website.

### Acknowledgements

- My mentor Juan Monetti who helped and explained me alot.
- Special thanks to the tutor team of Code Institute to answer all my questions I had during this milestone project.
- And all the other staff at Code Institute!