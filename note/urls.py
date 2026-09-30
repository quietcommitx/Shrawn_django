from django.urls import path, include
from .views import note_list, create_note
urlpatterns = [
   path('note/', note_list),
   path('create-note/', create_note)
]