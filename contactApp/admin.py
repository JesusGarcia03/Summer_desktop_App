from django.contrib import admin
from .models import Record, Profile, Post, Comment

# Register your models here.
admin.site.register(Record)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)