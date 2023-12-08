from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import json
from django.shortcuts import get_object_or_404
from .models import *
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def allPost(request):
    # get all posts in reverse chronological order
    posts_list = Posts.objects.all()
    posts_list = posts_list.order_by("-timestamp").all()
    paginator = Paginator(posts_list, 10)

    page_number = request.GET.get('page')
    posts_list = paginator.get_page(page_number)

    return render(request, "network/allPost.html", {
        "posts": posts_list
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("allPost"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("allPost"))
    

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("allPost"))
    else:
        return render(request, "network/register.html")

def create(request):
    posts_list = Posts.objects.all()
    posts_list = posts_list.order_by("-timestamp").all()
    post = Posts()

    if request.method == "POST":
        if request.POST.get('create_content'):
            post.content = request.POST.get('create_content')
            post.user = request.user
            post.save()

    return render(request, "network/allPost.html", {
        "posts": posts_list
    })

def profile(request, username):
    user = User.objects.get(username=username)
    posts_list = Posts.objects.filter(user=user)
    posts_list = posts_list.order_by("-timestamp").all()

    paginator = Paginator(posts_list, 10)
    page_number = request.GET.get('page')
    posts_list = paginator.get_page(page_number)

    # Followers
    followers = user.followers
    following_num = user.following_num

    current_user = request.user
    try:
        profile_temp = Followings.objects.get(user=user)
        followed = profile_temp.followed_by.all()
        if current_user in followed:   
            follow_btn = "Unfollow"
        else:
            follow_btn = "Follow"
    except Followings.DoesNotExist:
        follow_btn = "Follow"

    return render(request, "network/profile.html", {
        "username": username,
        "posts": posts_list,
        "followers": followers,
        "following_num": following_num,
        "follow_btn": follow_btn
    })

@login_required
@csrf_exempt
def like(request):
    user = request.user
    if request.method == "POST":
        postId = request.POST.get('postId')
        isLiked = request.POST.get('isLiked')
        post = Posts.objects.get(id=postId)
        if isLiked == "True":
            post.liked_by.remove(user)
            post.likes -= 1
        else:
            post.liked_by.add(user)
            post.likes += 1
        post.save()
        return JsonResponse({})
    return JsonResponse({}, status=400)

# the user follow the profile user
# add profile user in user.following
# add user in profile_user.followed_by
# return Json follower_num and button text Follow/Unfollow
def follow(request):
    user = request.user
    profile_username = request.GET.get("profile_user") or ""
    profile = get_object_or_404(User, username=profile_username)

    profile_user, _ = Followings.objects.get_or_create(user=user)

    profile_profile, _ = Followings.objects.get_or_create(user=profile)

    profile_follows = profile_profile.followed_by.all()
    follower_num = profile.followers

    if user in profile_follows:
        text = "Follow"
        profile.followers -= 1
        user.following_num -= 1
        profile_profile.followed_by.remove(user)
        profile_user.following.remove(profile)
    else:
        text = "Unfollow"
        profile.followers += 1
        user.following_num += 1
        profile_profile.followed_by.add(user)
        profile_user.following.add(profile)

    profile.save()
    user.save()
    profile_profile.save()
    profile_user.save()

    return JsonResponse({
        "text": text,
        "follower_num": follower_num
    })

# return all posts of followed users
# get followed users that current user following
# get all posts from followed users
def following(request):
    user = request.user
    try:
        profile_user = Followings.objects.get(user=user)
        followed_users = profile_user.following.all()
    except Followings.DoesNotExist:
        # Handle the case where Followings instance does not exist for the user
        followed_users = []
    
    posts_list = Posts.objects.filter(user__in=followed_users)
    posts_list = posts_list.order_by("-timestamp").all()

    paginator = Paginator(posts_list, 10)
    page_number = request.GET.get('page')
    posts_list = paginator.get_page(page_number)
    return render(request, "network/following.html", {
        "posts": posts_list,
    })

@login_required
@csrf_exempt
def edit(request):
    if request.method == "POST":
        postId = request.POST.get('postId')
        newContent = request.POST.get('newContent')
        post = Posts.objects.get(id=postId)
        post.content = newContent.strip()
        post.save()
        return JsonResponse({}, status=201)
    return JsonResponse({}, status=400)