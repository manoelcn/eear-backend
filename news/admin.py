from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'description', 'image',)
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
