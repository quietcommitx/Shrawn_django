from django.contrib import admin
from .models import Note
# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
   list_display = ('id','title','content')
   list_per_page = 5
   search_fields = ('title',)

# admin.site.register(Note, NoteAdmin)