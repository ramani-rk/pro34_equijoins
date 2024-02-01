from django.shortcuts import render

# Create your views here.

from app.models import *
from django.db.models import Q

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
    emo=Emp.objects.select_related('mgr').filter(empno__gte=50,deptno=30)


    d={'emo': emo}
    return render (request,'selfjoin.html',d)


def empmgrobject (request):
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter(empno__endswith=9)
    emd=Emp.objects.select_related('deptno','mgr').filter(empno__startswith=7)
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='Blake',mgr=7839)
    emd=Emp.objects.select_related('deptno','mgr').filter(job='Manager')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(ename='King') | Q(job='Salesman'))
    emd=Emp.objects.select_related('deptno','mgr').all()[0:10:3]
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=True)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=False)
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__gte=50000)
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__lte=5000)
    emd=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=False)
    emd=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=True)
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='Accounting')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='Sales')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno=10)
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno=20)
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno=30)
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__startswith='S')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dloc='Mumbai')
    emd=Emp.objects.select_related('deptno','mgr').filter(comm=None,sal__gte=5000)
    emd=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=True,sal__gte=10000)
    emd=Emp.objects.select_related('deptno','mgr').filter(hiredate__year=1981)
    emd=Emp.objects.select_related('deptno','mgr').filter(job='President',hiredate__year=1981)
    emd=Emp.objects.select_related('deptno','mgr').all()[0:10]
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter(hiredate__year__lte=1982,sal__lte=10000)
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(job='Salesman') | Q(mgr__isnull=True))



    d={'emd': emd}
    return render (request,'empmgrobject.html',d)
