from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Record, Post, Comment
from .forms import AddRecordForm, PostForm, SignUpForm, CommentForm


# --- Home View (display all records and posts) ---
@login_required
def home(request):
    records = Record.objects.all()
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'records': records, 'posts': posts})


# --- Add Record View ---
def add_record(request):
    if request.method == "POST":
        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = AddRecordForm()
    return render(request, 'add_record.html', {'forms': form})


# --- Create User Account ---
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # Creates the user
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})


# --- Create Post View (with image support) ---
@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "create_post.html", {"form": form})


# --- Post List View (optional, if you want a separate page for posts) ---
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})


# --- User Data View (show all registered users) ---
@login_required
def user_data(request):
    users = User.objects.all().order_by('username')
    return render(request, 'user_data.html', {'users': users})


# --- Add Comment View (text + optional image) ---
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("home")  # or redirect to post detail page if you have one
    else:
        form = CommentForm()
    return render(request, "add_comment.html", {"form": form, "post": post})
