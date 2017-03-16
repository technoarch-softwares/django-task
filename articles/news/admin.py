from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'created']
    search_fields = ['user__first_name', 'user__last_name', 'title']
    
admin.site.register(News, NewsAdmin)