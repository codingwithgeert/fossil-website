# The Fossil Shop

<div align="center">
<img src="#" alt="Screenshot" border="0"></a>
</div>
This webpage is a ecommerce webshop. It is made with Django. Customers can buy fossils and put them in a cart.
When they login they can see their cart history and order details.
After paid by Stripe there is an email sent with the user with their order detail.
The link to live page: [The Fossil Shop](https://the-fossil-shop.herokuapp.com/)


## UX
 
#### User Stories
- As a customer I want to search on the webpage for the item I want.

- As a customer I want to be able to create my own login account on the webpage.

- As a customer I want to have my items i clicked stored in a cart.

- As a customer I want to see a deatailed page of the item i clicked.

- As a customer I want to have a form to contact the developer of the website.

#### Design

The logo of the website is at the top left. Next to it are the navigation links to click to.
On mobile devices the navigation links are inside a hamburger icon.
When the user comes on the site it will see a carousel with pictures.
Beneath it is the webshop name and a slogan.
In the footer are some quick links the user can click which brings them to other pages.

### Wireframes

- [Desktop Homepage](#)
- [Desktop Edit page](#)
- [Mobile Homepage](#)


## Features

- <u>:</u>
- <u>Search bar:</u> Allow users to search for items in the webshop.
- <u>Detailed page</u> A link to the detailedpage where the user can see info about the product.
- <u>Add to Cart button<u> The user can click on this button and as an result it will be stored inside their cart.

### Features Left to Implement
- 
  




## Technologies Used

Tools:

- [Django](https://www.djangoproject.com/) 
    - The project uses **Django** as a framework.

- HTML
    -  standard markup language for this project.

- [AWS Cloud9](https://aws.amazon.com/cloud9/) 
    - **AWS Cloud9** used for their IDE while building and testing the website.
- CSS3
    - The project uses **CSS3** to style it.

- [GitHub](https://github.com/)
    - The project uses **GitHub** to store and share all project code to the github site.

- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) 
   - for the version control.

- [Postgress]()

- [Imgbb](https://imgbb.com) 
   - to upload all external images.

- [Heroku](https://www.heroku.com/)
    - The application is deployed to **heroku** 

- [JQuery](https://jquery.com) 
    - DOM manipulation.

- [Google Fonts](https://fonts.google.com/) 
    - for website fonts styles.

- [Font Awesome]()

Libraries

- [Bootstrap 4](https://https://getbootstrap.com/) as a framework.
 


## Testing

### Manual testing: 

All steps on desktop were repeated in browsers: Firefox, Chrome and Internet Explorer 

### Automatic test:

I used a unittest to test a GET function.
This is done by the code:  self.assertIn(b'Boar', result.data)
Where 'Boar' can be any data that is in the actual database/spotlist
If its in the database the test passed if its not it is failed.

#### Bugs
- 

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

### How to run this project locally

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

## Heroku Deployment

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
DEBUG | FALSE
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
PORT | 5000
SECRET_KEY | `<your_secret_key>`

- To get you MONGO_URI read the MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/)

8. In the heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed.


## Media

- 

## Code

- 
- testing code is from [Unittest](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn)
- 

### Acknowledgements

- My mentor Juan Monetti who helped and explained me alot.
- Special thanks to the tutor team of Code Institute to answer all my questions I had during this milestone project.
