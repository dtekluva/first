from django.shortcuts import render
from django.http import HttpResponse
from .models import mentor
from django.shortcuts import render

def index(request):
    all_mentor = mentor.objects.all()
    context = {'all_mentor' : all_mentor}
     
    return render(request, "page/index.html", context)



def detail(request, mentor_id):
    return HttpResponse("<h1>this a stdid  " + str(mentor_id) + "</h1>")




# Create your views here.


