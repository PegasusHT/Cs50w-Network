# Network

## Overview
A social network website that allows users to create, like posts, and follow other users.
The posts that all users created will be displayed in the homepage. The project is inspired from an exercise of a Harvard course, 
Cs50W - Web Development by Django and Python.<br>

## Features
### Log in, Log out
I used the login, logout template code of Cs50W exercise.

### Displaying all posts.
Initially, after we log inIf there are more than 10 posts, the page will show only 10 posts per page. 
There are buttons at the bottom of the page to navigate between posts.<br>
![All posts](/images/all-post.png)<br>
![Pagination buttons](/images/Pagination.png)

### User's profile
We can see a user's profile by clicking on his name.
The profile page will display the followers, following numbers, all of his posts, and a button for us to follow him.<br>
![Profile](/images/profile.png)<br>

### Like post
The user can click on the heart icon to like a post. 
The icon will change to the filled heart icon.
Click the icon again to unlike the post.
The behavior is implemented by JavaScript, so we don't need to re-render the page.<br>
![Like behavior](/images/like.png)<br>

## Run Application

1. You need to have python3. 
Then, you need to install pip and Django:
```shell
python3 -m ensurepip
pip3 install Django 
```

2. Run `python3 manage.py makemigrations network` to make migrations for the network app.

1. Run `python3 manage.py migrate` to apply migrations to your database

1. In the project4 directory, start the Django application.
```shell
python3 manage.py runserver
```

### Future Update
Move the hosting to AWS since they offer free basic tier service.