from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
  list_display = ('title', 'owner', 'status', 'created_at', 'updated_at')
  list_filter = ('status', 'owner')
  search_fields = ('title', 'description')
