from django import forms
from django.db.models.fields import CharField
from django.forms.widgets import SelectDateWidget
from .models import *
from student.models import *




class Lessonform(forms.ModelForm):
    class Meta:
        model = Lessons
        fields = ('course','subject','lesson_name','lesson_no','video','ppt','notes')








class LabCycleForm(forms.ModelForm):
    experiment_name=forms.CharField(max_length=100)
    experiment_aim=forms.Textarea()
    due_date=forms.DateField(widget=SelectDateWidget)
    
    class Meta:
        model=Lab_cycle
        fields=('subject','experiment_name','experiment_aim','due_date')


class LessonUpdateForm(forms.ModelForm):
    class Meta:
        model = Lessons
        fields = ('lesson_name','lesson_no','video','ppt','notes')

class MarkUploadForm(forms.ModelForm):
    mark=CharField(max_length=20)
    class Meta:
        model=Program
        fields=('mark',)