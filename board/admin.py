from django.contrib import admin
from .models import Board

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id','subscriber','title','content','created','updated']
    list_editable = ['title','content']
    raw_id_fields = ['subscriber']

admin.site.register(Board,BoardAdmin)