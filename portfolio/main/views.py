from django.shortcuts import render
from django.conf import settings
# Create your views here.
def index(request):
    context = {
        "name" : settings.DATA["NAME"],
    }
    print(context)
    return render(request, 'main/index.html',context)

def projects(request):
    context = {}
    return render(request, 'main/projects.html', context)