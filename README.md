# Project-LetsRise
A Yelp-like web application for connecting small businesses based in China

## Problem Definition
There are many entreprenuers in China working on several startups and businesses. As a freelancer based in China, problems that I faced were:
- I couldn't find an entrepreneur apart from the ones in my circle.
- It was difficult for people to reach out to me since marketing does not work the same way as it does in the other countries.
- It was difficult to find a legit business in China since many businesses are being formed everyday and the demand for quality and legit businesses were always high.
- Wechat groups have a limit of 500 members and it is very difficult to create a platform in wechat for foreigners in China to know about each other.

## Solution
Analyzing the problem and through realizing that there were no other startups in this field, I thought that I could create a baseline for anyone willing to start this startup. (If possible, I would work on this myself). I thought that certain features are necessary for this application and got inspired from Yelp.com to work on this project.

## Required features
- Login/Signup for members
- Post ads
- Blog posts
- Give ratings for ads of businesses
- Personally reviewing and checking the authenticity of a business before posting it
- Search for businesses on the application
- A custom profile page and getting matched with entrepreurs with similar interests

## Project Planning
To start off with the project, I created a plan and decided to allocate some time and work on it. I created a Gantt chart in excel and allocated my time according to the schedule.

![Alt text](github_images/gantt.png?raw=true "Title")

## Database design
I analyzed Yelp's User Interface and designed my database according to my requirements.

![Alt text](github_images/database.png?raw=true "Title")

## Project design
- Create a virtual environment
  ```python
   python -m virtualenv env
  ```
- Activate the virtual environment
  ```python
   . env/Scripts/activate
   ```
- Create the django project
   ```python
   django-admin startproject letsrise
    ```
- Create the apps
  ```python
   cd letsrise
   python manage.py startapp dashboard #The main app to manage ads and everything on the main page
   python manage.py startapp blog      #App to manage the blog
   python manage.py startapp user      #App to manage user profile, login, logout and singup
    ```
- To clone this project
  ```python
   git clone https://github.com/mcmuralishclint/Project-LetsRise.git
    ```
 
## Dashboard App 
The home page contains three search boxes. The search function can be used to search any ad by title, description, content, city and category. There is also a section for trending search which displays the top three most searched keywords.
![Alt text](github_images/dashboard/main.png?raw=true "Title")
There's a section for featured ads where premium ads can be displayed
![Alt text](github_images/dashboard/featured_ads.png?raw=true "Title")
There's a section to view ads by categories
![Alt text](github_images/dashboard/categories.png?raw=true "Title")
The latest blog posts are also dispayed on the home page
![Alt text](github_images/dashboard/featured_blog.png?raw=true "Title")
The ads page lists all the ads with a pagination included and each blog post is linked to a seperate page where users can create, delete and update their own posts.
![Alt text](github_images/dashboard/Ads_home.png?raw=true "Title")

### Blog App
All the blog posts are display on the blog page and each blog post has its unique page like the ad page.
![Alt text](github_images/blog/blog_home.png?raw=true "Title")

### User App
The login page for existing users (Facebook, linkdin, Instagram and Github included[Wechat will be added soon])
![Alt text](github_images/user/login.png?raw=true "Title")

Signup page for new users
![Alt text](github_images/user/signup.png?raw=true "Title")

### General
An About page
![Alt text](github_images/user/about.png?raw=true "Title")
A contact page
![Alt text](github_images/user/contact.png?raw=true "Title")

These are the main features and there are so many other features in the app which are not included above such Ratings, Validation, machine learning etc.
