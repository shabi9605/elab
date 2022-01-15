from django.contrib import admin
from . models import *
from django.contrib.admin.decorators import register

# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list_display=('user','course','status')

admin.site.register(Register,RegisterAdmin)


admin.site.register(Course)
admin.site.register(BlogModel)
admin.site.register(CommentModel)
admin.site.register(Announcement)
admin.site.register(Placement)
admin.site.register(Suggestions)
admin.site.register(Complaints)
admin.site.register(Review)
admin.site.register(Public)