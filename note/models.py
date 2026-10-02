from django.db import models

# Create your models here.
# TABLE: NOTE
# FIELDS: id, Title, Content, Program(Science,management, course_names), created_at

class Note(models.Model):
   title = models.CharField(max_length=50)
   content = models.TextField()
   created_at = models.DateField(null=True, auto_now_add=True)
   
   def __str__(self):
      return self.title

# models.py file create models -> 
# migration file: contains the state of models.py file(python manage.py makemigrations) -> 
# database reflect(python manage.py migrate)