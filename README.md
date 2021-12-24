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
In the project4 directory, start the Django application.
```shell
cd project4/
python3 manage.py runserver
```

