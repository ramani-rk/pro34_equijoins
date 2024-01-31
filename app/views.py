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
    EMO=Emp.objects.select_related('deptno').all()[2:7]
    EMO=Emp.objects.select_related('deptno').all()
    
    d={'EMO' : EMO}
    return render (request,'equijoin.html',d)



def selfjoin(request):

    emo=Emp.objects.select_related('mgr').all()
    emo=Emp.objects.select_related('mgr').filter(mgr__isnull=True)
    emo=Emp.objects.select_related('mgr').filter(ename__endswith='K')
    emo=Emp.objects.select_related('mgr').all()
    emo=Emp.objects.select_related('mgr').filter(hiredate__year=2023)
    emo=Emp.objects.select_related('mgr').filter(comm__gte=500)
    EMO=Emp.objects.select_related('mgr').filter(comm__isnull=False)
    emo=Emp.objects.select_related('mgr').filter(sal__lte=25000)
    emo=Emp.objects.select_related('mgr').filter(deptno=20)
    emo=Emp.objects.select_related('mgr').filter(sal__gte=50000)
    emo=Emp.objects.select_related('mgr').filter(deptno__dloc='Bengaluru')
    emo=Emp.objects.select_related('mgr').filter(deptno__dname='Analyst')
    emo=Emp.objects.select_related('mgr').filter(empno__gte=50)
    emo=Emp.objects.select_related('mgr').all()[0:10:3]
    emo=Emp.objects.select_related('mgr').filter(empno__gte=50,deptno=40)



    d={'emo': emo}
    return render (request,'selfjoin.html',d)