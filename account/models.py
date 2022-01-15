
from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.base import Model

from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone



# Create your models here.

class Course(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    course_name=models.CharField(max_length=50)
    course_code=models.CharField(max_length=20)
    def __str__(self):
        return str(self.course_name)


class Register(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    course=models.ForeignKey(Course,on_delete=models.CASCADE,default='Mathematics')
    address=models.TextField()
    phone=PhoneNumberField()
    image=models.ImageField(upload_to='images',blank=True,null=True)
    status=models.BooleanField(default=False)
    student='student'
    teacher='teacher'
    user_types=[
        (student,'student'),
        (teacher,'teacher')
    ]
    user_type=models.CharField(max_length=50,choices=user_types,default=student)
    def __str__(self):
        return str(self.user.username)


class BlogModel(models.Model):
    #id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    blog_title = models.CharField(max_length=20)
    blog = models.TextField()
    date=models.DateTimeField(default=timezone.now)
 
    def __str__(self):
        return f"Blog: {self.blog_title}"
 
class CommentModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    comment_text = models.TextField()
    blog = models.ForeignKey('BlogModel', on_delete=models.CASCADE)
     
    def __str__(self):
        return f"Commented on: {self.blog}"



class Announcement(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    announcement=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user.username)


class Placement(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=100)
    company_name=models.CharField(max_length=50)
    vaccancy=models.IntegerField()
    area=models.CharField(max_length=50)
    available_date=models.DateField()
    time=models.TimeField()
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user.username)


class Complaints(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    complaint=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user.username)


class Suggestions(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    suggestion=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user.username)


class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    one='1'
    two='2'
    three='3'
    four='4'
    five='5'
    ratings=[
        (one,'1'),
        (two,'2'),
        (three,'3'),
        (four,'4'),
        (five,'5')
    ]
    rating=models.CharField(max_length=6,choices=ratings,default=one)
    review=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user.username)



class Public(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    phone=PhoneNumberField()
    address=models.TextField()
    def __str__(self):
        return str(self.user.username)














