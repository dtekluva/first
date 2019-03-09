from django.contrib import admin
from .models import student
from .models import mentor
# Register your models here.


admin.site.register(mentor)
admin.site.register(student)