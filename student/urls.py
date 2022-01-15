from django.urls import path
from .import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('dashboard2',views.dashboard2,name='dashboard2'),
    path('student_view_lesson',views.student_view_lessons,name='student_view_lesson'),
    path('student_lesson_view',views.student_lesson_view,name='student_lesson_view'),
    path('subject_list/<int:course_id>',views.subject_list,name='subject_list'),
    path('upload_program/<int:lab_id>',views.upload_program,name='upload_program'),
    path('view_programs',views.view_programs,name='view_programs'),
    path('view_lab_cycle',views.view_lab_cycle,name='view_lab_cycle'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)