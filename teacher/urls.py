from django.urls import path
from .import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('dashboard1',views.dashboard1,name='dashboard1'),
    path('upload_study_material',views.upload_study_material,name='upload_study_material'),
    path('subject_list',views.subject_list,name='subject_list'),
    path('add_lesson',views.add_lesson,name='add_lesson'),
    #path('allsubject',views.allsubject,name='allsubject'),
    path('view_lessons',views.viewlessons,name='view_lessons'),
    path('lesson_view/<int:subject_id>',views.lesson_view,name='lesson_view'),
    path('upload_lab_cycle',views.upload_lab_cycle,name='upload_lab_cycle'),
    path('lesson_update/<int:lesson_id>',views.lesson_update,name='lesson_update'),
    path('lesson_delete/<int:lesson_id>',views.lesson_delete,name='lesson_delete'),
    path('upload_mark/<int:program_id>',views.upload_mark,name='upload_mark'),
    path('delete_lab_cycle/<int:experiment_id>',views.delete_lab_cycle,name='delete_lab_cycle'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)