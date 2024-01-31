from django.shortcuts import render

# Create your views here.

from app.models import *

def equijoin(request):
    EMO=Emp.objects.select_related('deptno').all()
    EMO=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    EMO=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    EMO=Emp.objects.select_related('deptno').all()
    EMO=Emp.objects.select_related('deptno').filter(deptno__dloc='Bengaluru')
    EMO=Emp.objects.select_related('deptno').filter(sal__gt=20000)
    EMO=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    EMO=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    EMO=Emp.objects.select_related('deptno').all()
    d={'EMO' : EMO}
    return render (request,'equijoin.html',d)