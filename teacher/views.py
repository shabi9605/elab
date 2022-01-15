
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import (DetailView, ListView, FormView, CreateView, UpdateView, DeleteView)
from .models import *
from . forms import *
from student.models import *

from django.http import HttpResponseRedirect, request
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.
def dashboard1(request):
    announcements=Announcement.objects.all().order_by('-date')
    return render(request,'dashboard1.html',{'announcements':announcements})

def upload_study_material(request):
    return render(request,'upload_study_material.html')


def subject_list(request):
    course=Course.objects.filter(user=request.user)

    
    print(course)
    
    print(request.user)
    
    

    return render(request,'course_list.html',{'course':course})


def add_lesson(request):
    User_instance=request.user.id
    print(User_instance)
    courses=Subject.objects.filter(course__user__id=User_instance)
    print(courses)

    if request.method=="POST":
        lesson_form=Lessonform(request.POST,request.FILES)
        if lesson_form.is_valid():
            lesson=lesson_form.save()
            lesson.save()
            messages.success(request,"Lesson Added Successfully")
            return render(request,'allsubject.html')
        else:
            return HttpResponse("Invalid Form")
    else:
        lesson_form=Lessonform()
    return render(request,'lesson_create.html',{'courses':courses,'form':lesson_form})


def viewlessons(request):
    User_instance=request.user.id
    #course_id__user__id=User_instance
    subject=Subject.objects.filter(course__user__id=User_instance)
    subject_id=Subject.objects.filter(course__user__id=User_instance)
    #id=Lessons.objects.get(id=id)
    print(subject_id)
    lessons=Lessons.objects.filter()
    print(lessons)
    print(request.user)
    return render(request,'view_lessons.html',{'lesson':lessons,'subject':subject})

def lesson_view(request,subject_id):
    print(subject_id)
    User_instance=request.user.id
    lesson=Lessons.objects.filter(subject=subject_id)
    print(lesson)
    return render(request,'lesson_view.html',{'lesson':lesson})


def upload_lab_cycle(request):
    experiment=Lab_cycle.objects.all().order_by('-date')

    if request.method=="POST":
        lab_cycle_form=LabCycleForm(data=request.POST)
        if lab_cycle_form.is_valid():
            lab_cycle_form=lab_cycle_form.save()
            subject=lab_cycle_form.subject
            #print(subject)
            course=Subject.objects.get(name=subject)
            print(course.course)
            lab_cycle_form.course=course.course
            lab_cycle_form.save()
            messages.success(request,"Experiment Added Successfully")
            return render(request,'upload_lab_cycle.html')
        else:
            return HttpResponse("Invalid Form")
    else:
        lab_cycle_form=LabCycleForm()
    return render(request,'upload_lab_cycle.html',{'lab_cycle_form':lab_cycle_form,'experiment':experiment})


def delete_lab_cycle(request,experiment_id):
    experiment=Lab_cycle.objects.get(id=experiment_id)
    experiment.delete()
    return redirect('upload_lab_cycle')


def lesson_update(request,lesson_id):
    lesson=Lessons.objects.get(id=lesson_id)
    lesson_update_form=LessonUpdateForm(instance=lesson)
    if request.method=="POST":
        lesson_update_form=LessonUpdateForm(request.POST,instance=lesson)
        lesson_update_form.save()
        return redirect('view_lessons')
    return render(request,'lesson_update.html',{'form':lesson_update_form})


def lesson_delete(request,lesson_id):
    lesson_delete=Lessons.objects.get(id=lesson_id)
    lesson_delete.delete()
    return redirect('view_lessons')

def upload_mark(request,program_id):
    mark=Program.objects.get(id=program_id)
    mark_form=MarkUploadForm(instance=mark)
    if request.method=="POST":
        mark_form=MarkUploadForm(request.POST,instance=mark)
        mark_form.save()
        return redirect('view_programs')
    return render(request,'upload_mark.html',{'mark_form':mark_form})









    


