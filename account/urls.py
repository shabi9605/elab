from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),


    path('public_register',views.public_register,name='public_register'),

    path('dashboard',views.dashboard,name='dashboard'),
    path('public_dashboard',views.public_dashboard,name='public_dashboard'),
    path('user_login',views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('allsubject',views.allsubject,name='allsubject'),
    path('update_profile',views.update_profile,name='update_profile'),
    
    path('blog/<int:_id>', views.BlogDetailView, name='blog'),
    
    path('blogs/', views.BlogListView, name='blogs'),
    path('chat',views.chat,name='chat'),

    path('add_announcement',views.add_announcement,name='add_announcement'),
    path('add_placement',views.add_placement,name='add_placement'),
    path('view_placement',views.view_placement,name='view_placement'),

    path('update_placement/<int:placement_id>',views.update_placement,name='update_placement'),
    path('delete_placement/<int:placement_id>',views.delete_placement,name='delete_placement'),

    path('add_suggestion',views.add_suggestion,name='add_suggestion'),
    path('view_suggestions',views.view_suggestions,name='view_suggestions'),

    path('add_complaints',views.add_complaints,name='add_complaints'),
    path('view_complaints',views.view_complaints,name='view_complaints'),

    path('add_rating',views.add_rating,name='add_rating'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

