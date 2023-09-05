from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

def insert_webpage(request):
    QSTO = Topic.objects.all()
    if request.method == 'POST':
        t_name = request.POST['TN']
        name = request.POST['NA']
        url = request.POST['UR']

        to = Topic.objects.get(topic_name=t_name)

        Wo = webpage.objects.get_or_create(topic_name=to,name=name,url=url)[0]
        Wo.save()

        QSWO = webpage.objects.all()

        return render(request,'display_webpage.html',{'QSWO':QSWO})

        return HttpResponse('<h1 style="color:green;">Data inserted to Webpage successfully</h1>')

    return render(request,'insert_webpage.html',{'QSTO':QSTO})


def insert_access(request):
    qswo = webpage.objects.all()
    d={'qswo':qswo}
    if request.method == 'POST':
        NA = request.POST['NA']
        dt = request.POST['DT']
        au = request.POST['AU']
        em = request.POST['Em']

        wo = webpage.objects.get(pk=NA)

        Ao = AccessRecord.objects.get_or_create(name=wo,date=dt,author=au,email=em)[0]
        Ao.save()

        qsao = AccessRecord.objects.all()

        return render(request,'display_access.html',{'qsao':qsao})

    return render(request,'insert_access.html',d)