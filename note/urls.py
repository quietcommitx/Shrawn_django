from django.urls import path, include
from .views import note_list, create_note, delete, edit
urlpatterns = [
   path('note/', note_list),
   path('create-note/', create_note),
   path('note/<id>/', edit),
   path('note/<id>/delete/', delete)
]