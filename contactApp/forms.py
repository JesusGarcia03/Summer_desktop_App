from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Record, Post

# --- Form for Record Model ---
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "First name", "class": "form-control"}),
        label=""
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Type last name", "class": "form-control"}),
        label=""
    )
    email = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Type valid email", "class": "form-control"}),
        label=""
    )
    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Type phone number", "class": "form-control"}),
        label=""
    )

    class Meta:
        model = Record
        exclude = ("user",)  # if you want to link to a user later

# --- Form for Post Model ---
class PostForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Post title", "class": "form-control"})
    )
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={"placeholder": "Write your post here...", "class": "form-control", "rows": 5})
    )

    class Meta:
        model = Post
        fields = ['title', 'content']
