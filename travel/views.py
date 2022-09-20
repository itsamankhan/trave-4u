from django.http import HttpResponse
from django.shortcuts import render
from feature.models import features

def home(request):
    features_data = features.objects.all()
    data = {
        'features_data':features_data
    }
    return render(request, "index.html",data)


def about(request):
    return render(request, "About_us.html")


def contact(request):
    try:
        user = request.GET['name']
        mail = request.GET['email']
        subject = request.GET['sub']
        text = request.GET['msg']
        data = {
            'user': 'user',
            'mail': 'mail',
            'subject': 'subject',
            'text': 'text'
        }

    except:
        pass
    return render(request, "contact.html")