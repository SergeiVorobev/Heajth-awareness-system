"""Define forms for user package"""
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Profile


class RegisterForm(UserCreationForm):
    """Class form for user registration"""

    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'First Name', 'class': 'form-control', }))
    last_name = forms.CharField(max_length=100, required=True,widget=forms.TextInput(
        attrs={'placeholder': 'Last Name', 'class': 'form-control', }))
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'class': 'form-control', }))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email',
    'class': 'form-control', }))
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control', 'data-toggle': 'password',
        'id': 'password', }))
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password', 'class': 'form-control',
        'data-toggle': 'password', 'id': 'password',}))

    class Meta:
        """
        Meta class for access to 'first_name', 'last_name', 'username', 'email', 'password1',
        'password2' data
        """
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    """Class form for updating user login"""

    username = forms.CharField(max_length=100, required=True,
    widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control', }))
    password = forms.CharField(max_length=50, required=True,
    widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control',
    'data-toggle': 'password', 'id': 'password', 'name': 'password', }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        """Meta class for access to 'username', 'password', 'remember_me' data"""
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    """Class form for updating user"""

    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        """Class Meta to access 'username', 'email' data"""
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    """Class form for updating user profile"""

    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        """Class Meta to access 'avatar' and 'bio' data"""
        model = Profile
        fields = ['avatar', 'bio']
