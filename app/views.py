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



def select_and_display(request):
    LTO = Topic.objects.all()
    d={'LTO':LTO}
    if request.method == 'POST':
        tnlist = request.POST.getlist('tn')
        QSWO = webpage.objects.none()
        
        for i in tnlist:
            QSWO = QSWO|webpage.objects.filter(topic_name=i)
        d1={'QSWO':QSWO}
        return render(request,'display_webpage.html',d1)
    return render(request,'select_and_display.html',d)


def checkbox(request):
    LTO = Topic.objects.all()
    d={'LTO':LTO}
    
    return render(request,'checkbox.html',d)


def New_one(request):
    QSTO = Topic.objects.all()
    d={'LTO':QSTO}
    if request.method == 'POST':
        tlist = request.POST.getlist('tn')
        QSWO = webpage.objects.none()
        QSAO = webpage.objects.none()
        for i in tlist:
            QSWO = QSWO|webpage.objects.filter(topic_name=i)
        for j in QSWO:
            QSAO = QSAO|AccessRecord.objects.filter(name=j.pk)
        
        d1={'QSWO':QSWO,'QSAO':QSAO}
        return render(request,'display_TS_AR.html',d1)
            
    return render(request,'select_and_display.html',d)