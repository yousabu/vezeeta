from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.widgets import PasswordInput
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserCreationForms(UserCreationForm):
    username=forms.CharField(label='اسم المستخدم')
    first_name= forms.CharField(label='الاسم الول')
    last_name=forms.CharField(label='الاسم الاخير')
    email = forms.EmailField(label='البريد الالكتروني')
    password1=forms.CharField(label='كلمه المرور' , widget=forms.PasswordInput(), min_length=5)
    password2=forms.CharField(label='تاكيد كلمه المرور',widget=forms.PasswordInput(),min_length=5)

   
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email','password1','password2')

class Youssef(forms.ModelForm):
    username = forms.CharField(label='اسم المستخدم')
    password = forms.CharField(label='كلمه المرور', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password')


class UpdateUserForm(forms.ModelForm):
    first_name= forms.CharField(label='الاسم الول')
    last_name=forms.CharField(label='الاسم الاخير')
    email = forms.EmailField(label='البريد الالكتروني')
    class Meta:
        model = User
        fields= ('first_name' , 'last_name' , 'email')

class UpdateProfileForm(forms.ModelForm):
   
    class Meta:
        model = Profile
        fields= ('name' , 'address', 'address_detail' , 'number_phone'
        , 'working_hours' , 'wating_time', 'who_i' , 'price'
        , 'facebook' , 'twitter', 'google' , 'join_new', 'type_of_person'
        , 'doctor', 'image' ,'specialist_doctor')