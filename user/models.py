"""Class models for user package"""
from django import forms
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """Class model for user profile"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    age = models.IntegerField(default=30)
    height = models.IntegerField(default=180)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        """save Profile data"""

        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            rgb_im = img.convert('RGB')
            rgb_im.save(self.avatar.path)

class UpdateUserForm(forms.ModelForm):
    """Form class for updating user credentials"""

    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        """Class Meta to access ''username', 'email' data"""
        model = User
        fields = ['username', 'email']

class UpdateProfileForm(forms.ModelForm):
    """Form class for updating user profile"""

    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    age = models.IntegerField(default=30)
    height = models.IntegerField(default=180)
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        """Class Meta to access 'avatar', 'age', 'height' and 'bio' data"""
        model = Profile
        fields = ['avatar', 'age', 'height', 'bio']
