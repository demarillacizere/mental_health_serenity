'''
Forms
'''
from datetime import timedelta
from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth import get_user_model
from tinymce.widgets import TinyMCE



User = get_user_model()


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


TITLE_CHOICES = {
    "MR": "Mr.",
    "MRS": "Mrs.",
    "MS": "Ms.",
}


class UserRegistrationForm(CustomUserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 m-3",
        'style': 'max-width: 300px;',
        'placeholder': 'Email'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 m-3",
        'style': 'max-width: 300px;',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 m-3",
        'style': 'max-width: 300px;',
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 m-3",
                'style': 'max-width: 300px;',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 m-3",
                'style': 'max-width: 300px;',
                'placeholder': 'Last Name'
            }),

        }


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width: 300px;', 'class': "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 m-3 "
                                                            }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5  "
                                                                 }))


class AddResourceForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title', 'style': 'width: 300px;', 'class': "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 m-3 "
                                                          }))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description of the Resource', 'style': 'width: 300px; height:200px', 'class': "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5  "
                                                                }))
    url = forms.URLField(widget=forms.URLInput(attrs={'placeholder': 'Title', 'style': 'width: 300px;', 'class': "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 m-3 "
                                                      }))
    picture = forms.ImageField(label='Upload Picture', required=False)
    class Meta:
        model = Resource
        fields = ['title', 'description', 'url', 'picture']

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'style': 'width: 300px;', 'class': "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 m-3", 'placeholder': 'Enter title'}),
            'content': TinyMCE(attrs={'class': 'form-control bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 m-3', 'placeholder': 'Enter content'}),
        }
# from datetime import datetime, timedelta

# class AppointmentForm(forms.ModelForm):
#     duration_choices = [
#         (30, '30 minutes'),
#         (45, '45 minutes'),
#         (60, '60 minutes'),
#     ]

#     date = forms.DateField(widget=AdminDateWidget())
#     start_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
#     duration = forms.ChoiceField(choices=duration_choices)

#     class Meta:
#         model = Appointment
#         fields = ['date', 'start_time', 'duration', 'purpose', 'status', 'professional']

#     def clean(self):
#         cleaned_data = super().clean()
#         start_time = cleaned_data.get("start_time")
#         duration = int(cleaned_data.get("duration"))

#         # Convert start_time to datetime for calculation
#         start_datetime = datetime.combine(datetime.min, start_time)

#         # Calculate end_time by adding duration to start_time
#         end_datetime = start_datetime + timedelta(minutes=duration)

#         # Extract time from end_datetime
#         end_time = end_datetime.time()

#         cleaned_data['end_time'] = end_time
#         return cleaned_data


# class Appointment(models.Model):
#     model = Appointment
#     exclude = ['user', 'first_name','last_name','email','profile_pic']

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ['user','email']
