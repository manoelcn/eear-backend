from django.contrib import admin
from .models import Exam


class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'file',)
    search_fields = ('title',)


admin.site.register(Exam, ExamAdmin)
