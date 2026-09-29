from django.shortcuts import render
from .models import Note
# Create your views here.
def note_list(request):
   notes = Note.objects.all()
   total = notes.count()
   context = {
      "notes": notes,
      "total":total
   }
   return render(request, 'note.html', context)

# create a model named todolist: title, decription, status(complete or not), ...., -> migrate   [ceate a table]
# use python shell to add date in todolist table
# create url, view: get all the data from todolist table,
# create a html page that display all the todolist details