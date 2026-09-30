from django.shortcuts import render, redirect
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

def create_note(request):
   if request.method == 'POST':
      req_title = request.POST.get('title')
      req_content = request.POST.get('content')
      # check if req_title and req_content is empty if empty then return error message, if not create a note(optional)
      Note.objects.create(title=req_title, content=req_content)
      return redirect('/note/')
   return render(request, 'create_note.html')


# create a model named todolist: title, decription, status(complete or not), ...., -> migrate   [ceate a table]
# use python shell to add date in todolist table
# create url, view: get all the data from todolist table,
# create a html page that display all the todolist details