
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import (DetailView, ListView, FormView, CreateView, UpdateView, DeleteView)
from teacher.models import *
from account.models import *
from . models import *
from account.views import *
import datetime



from django.http import HttpResponseRedirect, request
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

def dashboard2(request):
    update=Register.objects.filter(user_id=request.user.id)
    print(update)
    announcements=Announcement.objects.all().order_by('-date')
    return render(request,'dashboard2.html',{'update':update,'announcements':announcements})



def student_view_lessons(request):
    
    
    course=Course.objects.filter(course_name=request.user.register.course.course_name)
    
    
    #id=Lessons.objects.get(id=id)
    print(course)
    
    
    #print(lessons)
    print(request.user)
    return render(request,'student_view_lesson.html',{'course':course})



def student_lesson_view(request,subject_id):
    print(subject_id)
    User_instance=request.user.id
    lesson=Lessons.objects.filter(subject=subject_id)
    print(lesson)
    return render(request,'student_lesson_view.html',{'lesson':lesson})

def subject_list(request,course_id):
    subject=Subject.objects.filter(course=course_id)
    return render(request,'student_view_lesson.html',{'subject':subject})


def upload_program(request,lab_id):
    lab=Lab_cycle.objects.get(id=lab_id)
    print(lab)
    today_date=datetime.datetime.now().date()
    due_date=lab.due_date
    print(due_date)
    print(today_date)
    if today_date>due_date:
        a=True
    else:
        a=False
    
    
    if request.method=="POST":
        program_name=request.POST.get('program_name')
        program_file=request.FILES.get('program_file')
        Program.objects.create(
            lab_cycle=lab,
            program_name=program_name,
            program_file=program_file,
            user=request.user,
            due=a
            

        )
        return redirect('view_programs')
    else:
        return render(request,'upload_program.html')


def view_programs(request):
    no_due_programs=Program.objects.filter(due=False,lab_cycle__course=request.user.register.course)
    print(no_due_programs)
    due_programs=Program.objects.filter(due=True,lab_cycle__course=request.user.register.course)
    print(due_programs)
    student_due_program=Program.objects.filter(user=request.user,due=True).order_by('date')
    student_no_due_programs=Program.objects.filter(user=request.user,due=False).order_by('date')
    print(student_due_program)
    return render(request,'uploaded_programs.html',{'no_due_programs':no_due_programs,'student_no_due_programs':student_no_due_programs,'student_due_program':student_due_program,'due_programs':due_programs})




def view_lab_cycle(request):
    lab_cycle=Lab_cycle.objects.filter(course=request.user.register.course).order_by('-date')
    print(lab_cycle)
    return render(request,'view_lab_cycle.html',{'lab_cycle':lab_cycle})



