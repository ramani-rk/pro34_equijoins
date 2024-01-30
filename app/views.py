from django.shortcuts import render

# Create your views here.

from app.models import *

def equijoin(request):
    EMO=Emp.objects.select_related('deptno').all()
    d={'EMO' : EMO}
    return render (request,'equijoin.html',d)