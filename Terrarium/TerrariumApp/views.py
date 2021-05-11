from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import terrarium
from .formulaire import terrariumform


def index(request):
    if request.method=="POST":
        form = terrariumform(request.POST).save()

        return redirect('/terrarium')
    else:
   form = terrariumform()


return render(request, 'index.html', {'form':form})