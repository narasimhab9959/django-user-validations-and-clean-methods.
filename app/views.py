from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.froms import *


def sf(request):
    SFO=student_from()
    d={'SFO':SFO}
    if request.method =='POST':
        SFD=student_from(request.POST)
        if SFD.is_valid():
            return HttpResponse('is valid')
            
        else:
            return HttpResponse('in_valid')

    return render(request,'sf.html',d)