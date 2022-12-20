from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        #tn=request.POST['topic']
        tn=request.POST.get('topic')
        t=topic.objects.get_or_create(topic_name=tn)[0]
        t.save()
        return HttpResponse('Topic is inserted successfully')

    return render(request,'insert_topic.html')

def insert_webpage(request):
    topics=topic.objects.all()
    d={'topics':topics}

    if request.method=='POST':
        topic=request.POST['topics']
        na=request.POST['na']
        ur=request.POST['ur']
        t=topic.objects.get_or_create(topic_name=topic)[0]
        t.save()
        w=webpage.objects.get_or_create(topic_name=t,name=na,url=ur)[0]
        w.save()
        return HttpResponse('Webpage is inserted seuccessfully')
    return render(request,'insert_webpage.html',d)

def select_topic(request):
    topics=topic.objects.all()
    d={'topics':topics}

    if request.method=='POST':
        tn=request.POST.getlist('topic')
        print(tn)
        webpages=webpage.objects.none()
        for i in tn:
            webpages=webpages|webpage.objects.filter(topic_name=i)
        data={'webpages':webpages}
        return render(request,'display_webpage.html',data)
    return render(request,'select_topic.html',d)


def checkbox(request):
    topics=topic.objects.all()
    d={'topics':topics}
    
    return render(request,'checkbox.html',d)



