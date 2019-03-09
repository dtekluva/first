from django.db import models

# # Create your models here.

class mentor(models.Model):
     name = models.CharField(max_length=100)
     field = models.CharField(max_length=100, default = 'sex')
     def __str__(self):
         return self.name
   
  


 
class student(models.Model):
     name = models.CharField(max_length=100)
     field = models.CharField(max_length=100, default = 'sex')
     mentor = models.ForeignKey(mentor, on_delete=models.CASCADE)
     def __str__(self):
         return self.name
    






    

   