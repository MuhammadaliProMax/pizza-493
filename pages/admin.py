from django.contrib import admin
from pages.models import ScrollModel

# Register your models here.\
@admin.register(ScrollModel)
class ScrollModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discount', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['created_at', 'updated_at']
    ordering = ['-created_at']
