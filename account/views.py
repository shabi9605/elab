
import re
from django import http
from django.http.response import Http404
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect, request
from . forms import *
from . models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from teacher.models import *
from django.contrib import messages

# Create your views here.

def index(request):
    announcements=Announcement.objects.all().order_by('-date')
    return render(request,'index.html',{'announcements':announcements})

def register(request):
    reg=False
    
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=ProfileForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            
            profile.save()
            
            reg=True
            
            return HttpResponseRedirect('user_login')
        else:
            HttpResponse("Invalid Form")
    else:
        user_form=UserForm()
        profile_form=ProfileForm()
    return render(request,'register.html',{'register':reg,'user_form':user_form,'profile_form':profile_form})



def public_register(request):
    reg=False
    
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=PublicForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            
            profile.save()
            
            reg=True
            
            return HttpResponseRedirect('user_login')
        else:
            HttpResponse("Invalid Form")
    else:
        user_form=UserForm()
        profile_form=PublicForm()
    return render(request,'public_register.html',{'register':reg,'user_form':user_form,'profile_form':profile_form})





def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        
        try:
            user1=Register.objects.get(user=user)
        except:
            pass
            
        try:
            user2=Public.objects.get(user=user)
        except:
            pass
       
        if user:
            if user.is_active:
                try:
                    if user1:
                        active=Register.objects.all().filter(user_id=user.id,status=True)
                        if active:
                            login(request,user)
                            return HttpResponseRedirect(reverse('dashboard'))
                        else:
                            return HttpResponse("Waiting for approval")
                except:
                    pass

                try:
                    if user2:      
                        login(request,user)            
                        return HttpResponseRedirect(reverse('public_dashboard'))
                    else:
                        return HttpResponse("Waiting for approval")
                except:
                    pass
                try:
                    if user.is_superuser:
                        login(request,user)
                        return HttpResponseRedirect(reverse('dashboard'))
                    else:
                        return HttpResponse("Waiting for approval")
                except:
                    pass
            else:
                return HttpResponse("Not active")       
        else:
            return HttpResponse("Invalid username or password")
    else:
        return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')


def public_dashboard(request):
    return render(request,'public_dashboard.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

def allsubject(request):
    User_instance=request.user.id
    print(User_instance)
    courses=Subject.objects.filter(course__user__id=User_instance)
    print(courses)
    
    
    
    
    return render(request,'allsubject.html',{'courses':courses})


def update_profile(request):
        
    if request.method=="POST":
        update_form=UpdateForm(request.POST,instance=request.user)
        
        update_profile_form=UpdateProfileForm(request.POST,request.FILES,instance=request.user.register)
        if update_form.is_valid() and update_profile_form.is_valid():
            update_form.save()
            update_profile_form.save()
            messages.success(request,f'Your Account has been Updated')
            return redirect('dashboard')
    else:
        update_form=UpdateForm(instance=request.user)
        update_profile_form=UpdateProfileForm(instance=request.user.register)
    context={
        'update_form':update_form,
        'update_profile_form':update_profile_form
    }
    return render(request,'update_profile.html',context)


def chat(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            Post=BlogModel(user=request.user,blog_title=form.cleaned_data['blog_title'],
            blog=form.cleaned_data['blog'])
            Post.save()
            return HttpResponseRedirect('blogs')
        else:
            return HttpResponse('not valid')
    else:
        form=PostForm()
    return render(request,'chat.html',{'form':form})





def BlogListView(request):
    dataset = BlogModel.objects.all().order_by('-date')
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            blog = BlogModel.objects.get(blog_title=title)
            return redirect(f'/blog/{blog.id}')
    else:
        form = SearchForm()
    context = {
            'dataset':dataset,
            'form':form,
        }
    return render(request,'listview.html',context)


def BlogDetailView(request,_id):
    try:
        data =BlogModel.objects.get(id =_id)
        comments = CommentModel.objects.filter(blog = data)
    except BlogModel.DoesNotExist:
        raise Http404('Data does not exist')
     
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment = CommentModel(user=request.user,comment_text=form.cleaned_data['comment_text'],
            blog=data)
            Comment.save()
            return redirect(f'/blog/{_id}')
    else:
        form = CommentForm()
 
    context = {
            'data':data,
            'form':form,
            'comments':comments,
        }
    return render(request,'chat.html',context)





def add_announcement(request):
    if request.method=="POST":
        announcement_form=AnnouncementForm(request.POST)
        if announcement_form.is_valid():
            lv=Announcement(user=request.user,announcement=announcement_form.cleaned_data['announcement'])
            lv.save()
            return render(request,'announcement_form.html',{'msg':'successfully added announcement'})
        else:
            return HttpResponse("Invalid form")
    announcement_form=AnnouncementForm()
    return render(request,'announcement_form.html',{'announcement_form':announcement_form})



def add_placement(request):
    if request.method=="POST":
        placement_form=PlacementForm(request.POST)
        if placement_form.is_valid():
            lv=Placement(user=request.user,title=placement_form.cleaned_data['title'],company_name=placement_form.cleaned_data['company_name'],vaccancy=placement_form.cleaned_data['vaccancy'],area=placement_form.cleaned_data['area'],
            available_date=placement_form.cleaned_data['available_date'],time=placement_form.cleaned_data['time'])
            lv.save()
            return redirect('view_placement')
        else:
            return HttpResponse("Invalid form")
    placement_form=PlacementForm()
    return render(request,'placement_form.html',{'placement_form':placement_form})



def view_placement(request):
    placement=Placement.objects.all().order_by('-date')
    return render(request,'placements.html',{'placement':placement})



def update_placement(request,placement_id):
    placement=Placement.objects.get(id=placement_id)
    print(placement)
    update_placement_form=PlacementForm(instance=placement)
    if request.method=="POST":
        update_placement_form=PlacementForm(request.POST,request.FILES,instance=placement)
        update_placement_form.save()
        return redirect('view_placement')
    return render(request,'placement_form.html',{'placement_form':update_placement_form})



def delete_placement(request,placement_id):
    placement=Placement.objects.get(id=placement_id)
    placement.delete()
    return redirect('view_placement')



def add_suggestion(request):
    if request.method=="POST":
        suggestion_form=SuggestionForm(request.POST)
        if suggestion_form.is_valid():
            lv=Suggestions(user=request.user,suggestion=suggestion_form.cleaned_data['suggestion'])
            lv.save()
            return redirect('view_suggestions')
        else:
            return HttpResponse("Invalid form")
    suggestion_form=SuggestionForm()
    return render(request,'suggestion_form.html',{'suggestion_form':suggestion_form})


def view_suggestions(request):
    suggestions=Suggestions.objects.all().order_by('-date')
    my_suggestions=Suggestions.objects.filter(user=request.user).order_by('-date')
    return render(request,'view_suggestions.html',{'suggestions':suggestions,'my_suggestions':my_suggestions})



def add_complaints(request):
    if request.method=="POST":
        complaint_form=ComplaintForm(request.POST)
        if complaint_form.is_valid():
            lv=Complaints(user=request.user,complaint=complaint_form.cleaned_data['complaint'])
            lv.save()
            return redirect('view_complaints')
        else:
            return HttpResponse("Invalid form")
    complaint_form=ComplaintForm()
    return render(request,'complaint_form.html',{'complaint_form':complaint_form})


def view_complaints(request):
    complaint=Complaints.objects.all().order_by('-date')
    my_complaints=Complaints.objects.filter(user=request.user).order_by('-date')
    return render(request,'view_complaints.html',{'complaint':complaint,'my_complaints':my_complaints})


def add_rating(request):
    reviews=Review.objects.all().order_by('-date')
    if request.method=="POST":
        review_form=ReviewForm(request.POST)
        if review_form.is_valid():
            lv=Review(user=request.user,rating=review_form.cleaned_data['rating'],review=review_form.cleaned_data['review'])
            lv.save()
            return redirect('add_rating')
        else:
            return HttpResponse("Invalid form")
    review_form=ReviewForm()
    return render(request,'review_form.html',{'review_form':review_form,'reviews':reviews})





