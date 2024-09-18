from django.contrib import admin

# Register your models here.
from .models import Tasks

class MemberAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'task_description', 'task_status', 'created_at','updated_at','deleted_at')
admin.site.register(Tasks, MemberAdmin)