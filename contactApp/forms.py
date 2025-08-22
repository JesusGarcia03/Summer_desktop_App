from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record, Post, Comment


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
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Type valid email", "class": "form-control"}),
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


# --- Form for Post Model (with Image) ---
class PostForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Post title", "class": "form-control"})
    )
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            "placeholder": "Write your post here...",
            "class": "form-control",
            "rows": 5
        })
    )
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'image']


# --- Form for creating Users ---
class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


# --- Form for Comments (text + optional image) ---
class CommentForm(forms.ModelForm):
    text = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 3,
            "placeholder": "Write a comment..."
        })
    )
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={"class": "form-control mt-1"})
    )

    class Meta:
        model = Comment
        fields = ["text", "image"]
