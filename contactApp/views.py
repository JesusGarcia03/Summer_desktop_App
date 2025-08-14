from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Record, Post
from .forms import AddRecordForm, PostForm

# --- Home View (display all records and posts) ---
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
            return redirect('home')
    else:
        form = AddRecordForm()
    return render(request, 'add_record.html', {'forms': form})

# --- Create Post View ---
@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

# --- Post List View (optional, if you want a separate page for posts) ---
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})

def user_data(request):
    # Your logic here
    return render(request, 'user_data.html')