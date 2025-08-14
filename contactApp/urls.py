from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # home page showing records and posts
    path('record/add/', views.add_record, name='add_record'),  # add a record
    path('post/new/', views.create_post, name='create_post'),  # create a post
    path('posts/', views.post_list, name='post_list'),  # optional: list posts separately
    path('user/', views.user_data, name='user_data'),  # <-- this is required

]
