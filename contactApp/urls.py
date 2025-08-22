from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page showing records and posts
    path('record/add/', views.add_record, name='add_record'),  # Add a record
    path('post/new/', views.create_post, name='create_post'),  # Create a post
    path('posts/', views.post_list, name='post_list'),  # Optional: list posts separately
    path('user/', views.user_data, name='user_data'),  # Show all registered users
    path("accounts/", include("django.contrib.auth.urls")),  # Login/logout/password views
    path("accounts/signup/", views.signup, name="signup"),

    # --- Comment URL ---
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
]
