from re import T
from django import forms
from django.db.models import fields
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    username=forms.CharField(help_text=None,label='Username')
    password1=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Password')
    password2=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Confirm Password')
    
    class Meta:
        model=User
        fields=('username','password1','password2','email')
        labels=('password1','Password','password2','Confirm Password')

class ProfileForm(forms.ModelForm):
    address=forms.Textarea()
    image=forms.ImageField()
    student='student'
    teacher='teacher'
    
    user_types=[
        (student,'student'),
        (teacher,'teacher')
        
    ]
    user_type=forms.ChoiceField(required=True,choices=user_types)
    class Meta:
        model=Register
        fields=('address','phone','user_type','image','course')

class UpdateForm(forms.ModelForm):
    username=forms.CharField(help_text=None,label='Username')
    first_name=forms.CharField(help_text=None,label='firstname')
    last_name=forms.CharField(help_text=None,label='lastname')
    class Meta:
        model=User
        fields=('username','email','first_name','last_name')

class UpdateProfileForm(forms.ModelForm):
    address=forms.Textarea()
    image=forms.ImageField()
    class Meta:
        model=Register
        fields=('address','phone','image')


class PostForm(forms.ModelForm):
    blog=forms.CharField(help_text=None,label='Chat Content',widget=forms.Textarea())
    blog_title=forms.CharField(help_text=None,label='Chat Title')
    class Meta:
        model=BlogModel
        fields=('blog_title','blog')


class SearchForm(forms.Form):
    title = forms.CharField(max_length=20)


class CommentForm(forms.Form):
    #your_name =forms.CharField(max_length=20)
    comment_text =forms.CharField(widget=forms.Textarea)
 
    def __str__(self):
        return f"{self.comment_text} by {self.user.username}"
        


class AnnouncementForm(forms.ModelForm):
    announcement=forms.Textarea()
    class Meta:
        model=Announcement
        fields=('announcement',)


class PlacementForm(forms.ModelForm):
    available_date=forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model=Placement
        fields=('title','company_name','vaccancy','area','available_date','time')


class ComplaintForm(forms.ModelForm):
    complaint=forms.Textarea()
    class Meta:
        model=Complaints
        fields=('complaint',)





class SuggestionForm(forms.ModelForm):
    suggestion=forms.Textarea()
    class Meta:
        model=Suggestions
        fields=('suggestion',)



class ReviewForm(forms.ModelForm):
    review=forms.Textarea()
    class Meta:
        model=Review
        fields=('rating','review')


class PublicForm(forms.ModelForm):
    address=forms.Textarea()
    class Meta:
        model=Public
        fields=('phone','address')